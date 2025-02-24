from cnn_image_classifier import logger
from cnn_image_classifier.pipeline.one_data_ingestion import Data_Ingestion_Training_Pipeline
from cnn_image_classifier.pipeline.two_prepare_model import Prepare_Model_pipeline


if __name__ == '__main__':

    STAGE_NAME = 'Data_Ingestion'
    try:
        logger.info(f"++++++++Starting {STAGE_NAME} pipeline+++++++++")
        pipeline = Data_Ingestion_Training_Pipeline()
        pipeline.main()
        logger.info(f"++++++++Completed {STAGE_NAME} pipeline+++++++++")
    except Exception as e:
        logger.exception(e)
        raise e

    STAGE_NAME = 'Model_Preparation'
    try:
        logger.info(f"++++++++++++++Starting Stage: {STAGE_NAME} pipeline ++++++++++++++")
        pipeline = Prepare_Model_pipeline()
        pipeline.main()
        logger.info(f"++++++++++++++ Stage: {STAGE_NAME} pipeline Ended ++++++++++++++")
    except Exception as e:
        logger.error(e)