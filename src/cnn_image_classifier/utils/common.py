import os
from box.exceptions import BoxValueError
from cnn_image_classifier import logger
import yaml
import json
import joblib
from ensure import ensure_annotations
from typing import Any
from box import ConfigBox
from pathlib import Path
import base64

@ensure_annotations
def read_yaml_file(filepath: Path) -> ConfigBox:
    """Read a yaml file and return a ConfigBox object."""
    try:
        with open(filepath, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file:{filepath.name} has been read successfully.') 
            return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError(f'Error reading yaml file: {filepath.name}')
    except Exception as e:
        raise e

@ensure_annotations
def save_json(filepath:Path ,data:dict):
    """Save a dictionary to a json file."""
    try:
        with open(filepath, 'w') as json_file:
            json.dump(data, json_file, indent=4)
            logger.info(f'json file:{filepath.name} has been saved successfully.')
    except Exception as e:
        raise e

@ensure_annotations
def load_json(filepath:Path )->ConfigBox:
    """loading json file and return a ConfigBox object."""
    try:
        with open(filepath, 'r') as json_file:
            content = json.load(json_file)
            logger.info(f'json file:{filepath.name} has been loaded successfully.')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f'Error reading json file: {filepath.name}')
    except Exception as e:
        raise e 

@ensure_annotations
def save_bin(filepath:Path ,data:Any):
    """Save a binary file."""
    try:
        with open(filepath, 'wb') as bin_file:
            joblib.dump(data, bin_file)
            logger.info(f'binary file:{filepath.name} has been saved successfully.')
    except Exception as e:
        raise e

@ensure_annotations
def load_bin(filepath:Path)->Any:
    """loading binary file."""
    try:
        with open(filepath, 'rb') as bin_file:
            content = joblib.load(bin_file)
            logger.info(f'binary file:{filepath.name} has been loaded successfully.')
            return content
    except Exception as e:
        raise e

@ensure_annotations
def getsize(filepath:Path)->str:
    """Get the size of a file."""
    try:
        size_kb = round(os.path.getsize(filepath)/1024)
        return f'{size_kb} KB'
    except Exception as e:
        raise e

@ensure_annotations
def encode_image_to_base64(imagepath:Path)->str:
    """Encode an image to base64."""
    try:
        with open(imagepath, 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            return encoded_string
    except Exception as e:
        raise e

@ensure_annotations
def decode_base64_to_image(base64_string:str, imagepath:Path):
    """Decode a base64 string to an image."""
    try:
        with open(imagepath, 'wb') as image_file:
            image_file.write(base64.b64decode(base64_string))
    except Exception as e:
        raise e


