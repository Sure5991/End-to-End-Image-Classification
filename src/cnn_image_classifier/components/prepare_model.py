from pathlib import Path
import tensorflow as tf
import os
from cnn_image_classifier.config.configuration import BaseModelConfig
from cnn_image_classifier import logger

class prepare_base_model:
    def __init__(self, config: BaseModelConfig):
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.applications.VGG16(
            input_shape = self.config.params_image_size,
            include_top = self.config.params_include_top,
            weights = self.config.params_weights,)
        self.save_model(path = self.config.base_model_path, model = self.model)
        logger.info(f'Base model saved at : {self.config.base_model_path}')

    @staticmethod
    def prepare_full_model(model,classes,freeze_all,freeze_till,learning_rate):
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0 ):
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False
        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(classes, activation = 'softmax')(flatten_in)
        full_model = tf.keras.models.Model(inputs = model.input, outputs = prediction)
        
        full_model.compile(
            optimizer = tf.keras.optimizers.SGD(learning_rate = learning_rate),
            loss = 'categorical_crossentropy',
            metrics = ['accuracy']
            )
        full_model.summary()
        return full_model

    def update_base_model(self):
        self.full_model = self.prepare_full_model(
            model = self.model,
            classes = self.config.params_classes,
            freeze_all = True,
            freeze_till = None,
            learning_rate = self.config.learning_rate
    )

        self.save_model(path = self.config.updated_model_path, model = self.full_model)
        logger.info(f'Updated model saved at : {self.config.updated_model_path}')

    @staticmethod
    def save_model(path: Path, model: tf.keras.models.Model):
        model.save(path)
        
