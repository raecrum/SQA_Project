import logging
import os


def giveMeLoggingObject():
    format_str = '%(asctime)s:%(levelname)s:%(message)s'
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs')
    os.makedirs(log_dir, exist_ok=True)
    file_name = os.path.join(log_dir, 'SQA.log')
    logging.basicConfig(format=format_str, filename=file_name, level=logging.INFO)
    return logging.getLogger('sqa-logger')
