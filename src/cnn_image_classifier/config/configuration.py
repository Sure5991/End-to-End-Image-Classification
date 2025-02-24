from cnn_image_classifier.constants import *
from cnn_image_classifier.utils.common import read_yaml_file, create_directories
from cnn_image_classifier.entity.config_entity import *

class Config_Manager:
    def __init__(self, config_file_path: Path = config_path, param_file_path: Path = param_path):
        self.config = read_yaml_file(config_file_path)
        self.params = read_yaml_file(param_file_path)
        create_directories([self.config.artifact_root])

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir = Path(config.root_dir),
            source = Path(config.source),
            local_data_file = Path(config.local_data_file),
            unzip_dir = Path(config.unzip_dir)
        )

        return data_ingestion_config

    def get_base_model_config(self) -> BaseModelConfig:
        config = self.config.prepare_base_model
        create_directories([config.root_dir])
        prepare_base_model_config = BaseModelConfig(
            root_dir = Path(config.root_dir),
            base_model_path = Path(config.base_model),
            updated_model_path = Path(config.base_model_updated),
            params_image_size = self.params.image_size,
            params_weights = self.params.weights,
            params_include_top = self.params.include_top,
            params_classes = self.params.classes,
            learning_rate = self.params.learning_rate
        )

        return prepare_base_model_config



        


