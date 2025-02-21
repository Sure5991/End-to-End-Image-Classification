from cnn_image_classifier.config.configuration import Config_Manager
from cnn_image_classifier.components.data_ingestion import DataIngestion 
from cnn_image_classifier import logger

STAGE_NAME = 'Data_Ingestion'

class Data_Ingestion_Training_Pipeline:
    def __init__(self):
        pass
    
    def main(self):
        configuration_manager = Config_Manager()
        data_ingestion_config = configuration_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_data()

if __name__ == '__main__':
    try:
        logger.info(f"++++++++Starting {STAGE_NAME} pipeline+++++++++")
        pipeline = Data_Ingestion_Training_Pipeline()
        pipeline.main()
        logger.info(f"++++++++Completed {STAGE_NAME} pipeline++++++++\n\nx===================x")
    except Exception as e:
        logger.exception(e)
        raise e


