from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source: Path
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen = True)
class BaseModelConfig:
    root_dir: Path
    base_model_path : Path
    updated_model_path : Path
    params_image_size : list
    params_weights : str
    params_include_top : bool
    params_classes : int
    learning_rate : float