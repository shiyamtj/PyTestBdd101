import logging
import time
from pathlib import Path

class Logger:
    def __init__(self, logger, file_level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)-15s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')

        current_time = time.strftime("%Y_%B_%d")
        base_path = Path(__file__).parent
        self.log_file_name = (base_path / f'../logs/log_{current_time}.txt')

        # "a" to append the logs in same file, "w" to generate new logs and delete old one
        fh = logging.FileHandler(self.log_file_name, mode="a")
        fh.setFormatter(formatter)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)
