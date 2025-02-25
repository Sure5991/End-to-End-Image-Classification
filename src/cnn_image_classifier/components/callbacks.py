import tensorflow as tf
import time
import os
from cnn_image_classifier.entity.config_entity import Callback_Config
from cnn_image_classifier.config.configuration import Config_Manager
from cnn_image_classifier import logger

class Prepare_Callback:
    def __init__(self, config : Callback_Config):
        self.config = config

    @property
    def create_tb_callback(self):
        timestamp = time.strftime("%Y_%m_%d-%H:%M:%S")
        tb_running_log_dir = os.path.join(self.config.tensorboard_dir,f'tb_logs_at_{timestamp}')
        return tf.keras.callbacks.TensorBoard(log_dir = tb_running_log_dir)
    
    @property
    def create_checkpoint_callback(self):
        return tf.keras.callbacks.ModelCheckpoint(filepath = self.config.model_checkpoint,
                                                  save_best_only = True,)
    
    def get_callbacks(self):
        logger.info('callbacks initiated')
        return [self.create_tb_callback, self.create_checkpoint_callback]
    

if (__name__) == "__main__":
    try:
        config = Config_Manager()
        callback_config = config.get_callbacks_config()
        callback = Prepare_Callback(config = callback_config)
        callback_list = callback.get_callbacks()
    except Exception as e:
        logger.error(e)
        raise e