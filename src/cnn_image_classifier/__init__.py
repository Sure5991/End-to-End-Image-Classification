import os
import sys
import logging
from datetime import datetime

logging_str = "[%(asctime)s : %(levelname)s : %(module)s] - %(message)s"
log_dir = 'logs'
log_file =  f"{datetime.now().strftime('%d-%m-%Y')}.log"
os.makedirs(log_dir, exist_ok=True)
logpath = os.path.join(log_dir,log_file)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers = [
        logging.FileHandler(logpath),
        logging.StreamHandler(sys.stdout)
    ]
    )
logger = logging.getLogger('cnn_classifier')