#template.py

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format = '[%(asctime)s] %(levelname)s : %(message)s')
project_name = 'cnn_image_classifier'
list_of_files = ['.github/workflows/.gitkeep',
                 f'src/{project_name}/__init__.py',
                 f'src/{project_name}/components/__init__.py',
                 f'src/{project_name}/utils/__init__.py',
                 f'src/{project_name}/config/configuration.py',
                 f'src/{project_name}/pipeline/__init__.py',
                 f'src/{project_name}/entity/__init__.py',
                 f'src/{project_name}/constants/__init__.py',
                 'config/config.yaml',
                 'dvc.yaml',
                 'params.yaml',
                 'requirements.txt',
                 'setup.py',
                 'research/trails.ipynb',
                 'templates/index.html'
                 ]

for file_path in list_of_files:
    filepath = Path(file_path)
    filedir,filename = os.path.split(filepath)

    if filedir and not os.path.exists(filedir):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Directory created: {filedir} for the file : {filename}')
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            logging.info(f'File created: {filename}')
            pass
    else:
        logging.info(f'File already exists: {filename}')

        
