from typing import Any, Dict, List, Optional, Tuple
import copy
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader

#from data import MNISTDataset, FederatedSampler
#from models.models import CNN, MLP
from models.models import CNN, MLP
from utils import arg_parser, average_weights, Logger
from data.mnist import MNISTDataset
from data.sampler import FederatedSampler
from core.sampler_builder import get_sampler
from core.client_selection import ClientSelector

class FedAvg:
    """Implementation of FedAvg
    http://proceedings.mlr.press/v54/mcmahan17a/mcmahan17a.pdf
    """

    def __init__(self, args: Dict[str, Any]):
        self.args = args
        self.device = torch.device(
            f"cuda:{args.device}" if torch.cuda.is_available() else "cpu"
        )
        self.logger = Logger(args)

        self.train_loader, self.test_loader = self._get_data(
            root=self.args.data_root,
            n_clients=self.args.n_clients,
            n_shards=self.args.n_shards,
            non_iid=self.args.non_iid,
            sample_type=self.args.sample_type
        )

        if self.args.model_name == "mlp":
            self.root_model = MLP(input_size=784, hidden_size=128, n_classes=10).to(
                self.device
            )
            self.target_acc = 0.97
        elif self.args.model_name == "cnn":
            self.root_model = CNN(n_channels=1, n_classes=10).to(self.device)
            self.target_acc = 0.99
        else:
            raise ValueError(f"Invalid model name, {self.args.model_name}")

        self.reached_target_at = None  # type: int

    def _get_data(self,
            root: str,
            n_clients: int,
            n_shards: int,
            non_iid: int,
            sample_type: str
    ) -> Tuple[DataLoader, DataLoader]:
        """
        Args:
            root (str): path to the dataset.
            n_clients (int): number of clients.
            n_shards (int): number of shards.
            non_iid (int): 0: IID, 1: Non-IID
            sample_type (int): federated, uniform, group, responsive

        Returns:
            Tuple[DataLoader, DataLoader]: train_loader, test_loader
        """
        global sampler, train_loader

        train_set = MNISTDataset(root=root, train=True)
        test_set = MNISTDataset(root=root, train=False)

        if sample_type == 'federated':
            sampler = FederatedSampler(
                train_set,
                non_iid=non_iid,
                n_clients=n_clients,
                n_shards=n_shards
            )
            train_loader = DataLoader(train_set, batch_size=128, sampler=sampler)
        elif sample_type == 'uniform':
            sampler = get_sampler(
                sample_strategy=sample_type,
                client_num=n_clients,
            )
            train_loader = DataLoader(train_set,
                                      batch_size=128,
                                      sampler=sampler.sample(size=n_clients))
        elif sample_type == 'group':
            sampler = get_sampler(
                sample_strategy=sample_type,
                client_num=n_clients,
            )
            train_loader = DataLoader(train_set,
                                      batch_size=128,
                                      sampler=sampler.sample(size=n_clients, shuffle=True))
        elif sample_type == 'responsiveness':
            sampler = get_sampler(
                sample_strategy=sample_type,
                client_num=n_clients,
            )
            train_loader = DataLoader(train_set, batch_size=128, sampler=sampler.sample(size=n_clients))


        # train_loader = DataLoader(train_set, batch_size=128, sampler=sampler)
        test_loader = DataLoader(test_set, batch_size=128)

        return train_loader, test_loader

    def _train_client(
        self, root_model: nn.Module, train_loader: DataLoader, client_idx: int
    ) -> Tuple[nn.Module, float]:
        """Train a client model.

        Args:
            root_model (nn.Module): server model.
            train_loader (DataLoader): client data loader.
            client_idx (int): client index.

        Returns:
            Tuple[nn.Module, float]: client model, average client loss.
        """
        model = copy.deepcopy(root_model)
        model.train()
        optimizer = torch.optim.SGD(
            model.parameters(), lr=self.args.lr, momentum=self.args.momentum
        )

        for epoch in range(self.args.n_client_epochs):
            epoch_loss = 0.0
            epoch_correct = 0
            epoch_samples = 0

            for idx, (data, target) in enumerate(train_loader):
                data, target = data.to(self.device), target.to(self.device)
                optimizer.zero_grad()

                logits = model(data)
                loss = F.nll_loss(logits, target)
                loss.backward()
                optimizer.step()

                epoch_loss += loss.item()
                epoch_correct += (logits.argmax(dim=1) == target).sum().item()
                epoch_samples += data.size(0)

            # Calculate average accuracy and loss
            epoch_loss /= idx
            epoch_acc = epoch_correct / epoch_samples

            print(
                f"Client #{client_idx} | Epoch: {epoch}/{self.args.n_client_epochs} | Loss: {epoch_loss} | Acc: {epoch_acc}",
                end="\r",
            )

        return model, epoch_loss / self.args.n_client_epochs

    def train(self) -> None:
        """Train a server model."""
        train_losses = []
        global idx_clients

        for epoch in range(self.args.n_epochs):
            clients_models = []
            clients_losses = []

            # Randomly select clients
            m = max(int(self.args.frac * self.args.n_clients), 1)
            if self.args.sample_type == 'random':
                # idx_clients = np.random.choice(range(self.args.n_clients), m, replace=False)
                selector = ClientSelector(self.args.n_clients)
                idx_clients = selector.random_selection(m)
            elif self.args.sample_type == 'replacement':
                selector = ClientSelector(self.args.n_clients)
                idx_clients = selector.random_selection_with_replacement(m)
            elif self.args.sample_type == 'stratified':
                labels = np.random.randint(0, 10, self.args.n_clients)
                selector = ClientSelector(self.args.n_clients)
                idx_clients = selector.stratified_sampling(m, labels)
            elif self.args.sample_type == 'active-learning':
                uncertainty_scores = np.random.rand(self.args.n_clients)
                selector = ClientSelector(self.args.n_clients)
                idx_clients = selector.active_learning(m, uncertainty_scores)
            elif self.args.sample_type == 'cohort':
                cohort_labels = np.random.choice(['A', 'B', 'C'], self.args.n_clients)
                selector = ClientSelector(m, self.args.n_clients)
                idx_clients = selector.cohort_selection(m, cohort_labels)
            elif self.args.sample_type == 'rank':
                client_features = np.random.rand(self.args.n_clients)
                client_performance = np.random.rand(self.args.n_clients)
                selector = ClientSelector(self.args.n_clients)
                idx_clients = selector.learning_to_rank_selection(m, client_features, client_performance)
            elif self.args.sample_type == 'budget':
                budget = 100  # Budget for communication or computation
                client_costs = np.random.randint(1, 10, self.args.n_clients)
                selector = ClientSelector(self.args.n_clients)
                idx_clients = selector.budget_constrained_selection(budget, client_costs)
            elif self.args.sample_type == 'reputation':
                reputation_scores = np.random.rand(self.args.n_clients)
                selector = ClientSelector(self.args.n_clients)
                idx_clients = selector.reputation_selection(m, reputation_scores)
            elif self.args.sample_type == 'priority':
                priority_scores = np.random.rand(self.args.n_clients)
                selector = ClientSelector(self.args.n_clients)
                idx_clients = selector.priority_selection(m, priority_scores)

            # Train clients
            self.root_model.train()

            for client_idx in idx_clients:
                # Set client in the sampler
                self.train_loader.sampler.set_client(client_idx)

                # Train client
                client_model, client_loss = self._train_client(
                    root_model=self.root_model,
                    train_loader=self.train_loader,
                    client_idx=client_idx,
                )
                clients_models.append(client_model.state_dict())
                clients_losses.append(client_loss)

            # Update server model based on clients models
            updated_weights = average_weights(clients_models)
            self.root_model.load_state_dict(updated_weights)

            # Update average loss of this round
            avg_loss = sum(clients_losses) / len(clients_losses)
            train_losses.append(avg_loss)

            if (epoch + 1) % self.args.log_every == 0:
                # Test server model
                total_loss, total_acc = self.test()
                avg_train_loss = sum(train_losses) / len(train_losses)

                # Log results
                logs = {
                    "train/loss": avg_train_loss,
                    "test/loss": total_loss,
                    "test/acc": total_acc,
                    "round": epoch,
                }
                if total_acc >= self.target_acc and self.reached_target_at is None:
                    self.reached_target_at = epoch
                    logs["reached_target_at"] = self.reached_target_at
                    print(
                        f"\n -----> Target accuracy {self.target_acc} reached at round {epoch}! <----- \n"
                    )

                self.logger.log(logs)

                # Print results to CLI
                print(f"\n\nResults after {epoch + 1} rounds of training:")
                print(f"---> Avg Training Loss: {avg_train_loss}")
                print(
                    f"---> Avg Test Loss: {total_loss} | Avg Test Accuracy: {total_acc}\n"
                )

                # Early stopping
                if self.args.early_stopping and self.reached_target_at is not None:
                    print(f"\nEarly stopping at round #{epoch}...")
                    break

    def test(self) -> Tuple[float, float]:
        """Test the server model.

        Returns:
            Tuple[float, float]: average loss, average accuracy.
        """
        self.root_model.eval()

        total_loss = 0.0
        total_correct = 0.0
        total_samples = 0

        for idx, (data, target) in enumerate(self.test_loader):
            data, target = data.to(self.device), target.to(self.device)

            logits = self.root_model(data)
            loss = F.nll_loss(logits, target)

            total_loss += loss.item()
            total_correct += (logits.argmax(dim=1) == target).sum().item()
            total_samples += data.size(0)

        # calculate average accuracy and loss
        total_loss /= idx
        total_acc = total_correct / total_samples

        return total_loss, total_acc


if __name__ == "__main__":
    args = arg_parser()
    fed_avg = FedAvg(args)
    fed_avg.train()
