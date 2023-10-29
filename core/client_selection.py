import numpy as np

class ClientSelector:
    def __init__(self, num_clients):
        self.num_clients = num_clients

    def random_selection(self, m):
        # Randomly select m clients
        return np.random.choice(range(self.num_clients), m, replace=False)

    def stratified_sampling(self, m, labels):
        # Stratified sampling based on client labels
        unique_labels = np.unique(labels)
        selected_clients = []
        for label in unique_labels:
            label_indices = np.where(labels == label)[0]
            num_per_label = min(m // len(unique_labels), len(label_indices))
            selected_clients.extend(np.random.choice(label_indices, num_per_label, replace=False))
        return selected_clients

    def active_learning(self, m, uncertainty_scores):
        # Active learning: select clients with high uncertainty scores
        selected_clients = np.argsort(uncertainty_scores)[-m:]
        return selected_clients