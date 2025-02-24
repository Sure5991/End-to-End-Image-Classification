from cnn_image_classifier.config.configuration import Config_Manager
from cnn_image_classifier.components.prepare_model import prepare_base_model
from cnn_image_classifier import logger

stage_name = "Prepare Model"

class Prepare_Model_pipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = Config_Manager()
            base_model_config = config.get_base_model_config()
            modal = prepare_base_model(base_model_config)
            modal.get_base_model()
            modal.update_base_model()
        except Exception as e:
            raise e

if __name__ == "__main__":
    try:
        logger.info(f"++++++++++++++Starting Stage: {stage_name} pipeline ++++++++++++++")
        pipeline = Prepare_Model_pipeline()
        pipeline.main()
        logger.info(f"++++++++++++++ Stage: {stage_name} pipeline Ended ++++++++++++++")
    except Exception as e:
        logger.error(e)