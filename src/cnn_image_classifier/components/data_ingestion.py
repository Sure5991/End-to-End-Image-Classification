import os
import zipfile
import gdown
from cnn_image_classifier import logger
from cnn_image_classifier.utils.common import getsize
from cnn_image_classifier.config.configuration import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):            
            url = f"https://drive.google.com/uc?id={self.config.source}"
            save_path = self.config.local_data_file
            gdown.download(url, str(save_path), quiet=False)            
            logger.info(f"Data downloaded at {self.config.local_data_file}")
        else:
            logger.info(f"Data already exists at {self.config.local_data_file}")
    def extract_data(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

