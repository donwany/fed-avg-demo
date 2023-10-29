from dataclasses import  dataclass

@dataclass()
class Processing:
    batch_size: int = 64
    max_length: int = 1024