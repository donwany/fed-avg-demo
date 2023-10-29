import hydra
from omegaconf import DictConfig, OmegaConf
import os
from utils import Processing
from hydra.core.config_store import ConfigStore

@hydra.main(version_base=None, config_path="configs", config_name="config")
def main(cfg: DictConfig) -> None:
    """Using Config Yaml files approach"""
    print(OmegaConf.to_yaml(cfg))
    print('-'*50)
    print(cfg.model.tokenizer)
    print(cfg.processing.batch_size)
    assert cfg.processing.batch_size == 64
    assert isinstance(cfg.processing.batch_size, int)
    print(cfg.processing.max_length)
    print(cfg.training.log_every_n_steps)
    print(cfg.training.deterministic)
    print(cfg.training.limit_train_batches)
    print(cfg.training.limit_val_batches)
    print('-'*50)
    print(f"Working directory : {os.getcwd()}")
    print(f"Output directory  : {hydra.core.hydra_config.HydraConfig.get().runtime.output_dir}")


cs = ConfigStore.instance()
cs.store(name="configs", node=Processing)
@hydra.main(version_base=None, config_name="configs")
def my_app(cfg: Processing) -> None:
    """Using Data classes approach"""
    if cfg.batch_size == 64:
        print("Current batch size is ...")


if __name__ == "__main__":
    main()
    print('-'*50)
    my_app()
