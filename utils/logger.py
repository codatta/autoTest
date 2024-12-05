import logging
import os


def setup_logger():
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    logger = logging.getLogger('automated_testing')
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(os.path.join(log_dir, 'test.log'))
    logger.addHandler(file_handler)
    return logger


logger = setup_logger()