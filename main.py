from cnn_image_classifier import logger
from cnn_image_classifier.pipeline.data_ingestion import Data_Ingestion_Training_Pipeline

STAGE_NAME = 'Data_Ingestion'

if __name__ == '__main__':
    try:
        logger.info(f"++++++++Starting {STAGE_NAME} pipeline+++++++++")
        pipeline = Data_Ingestion_Training_Pipeline()
        pipeline.main()
        logger.info(f"++++++++Completed {STAGE_NAME} pipeline+++++++++)
    except Exception as e:
        logger.exception(e)
        raise e