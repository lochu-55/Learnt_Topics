import logging
import os


class CustomLogging:
    def __init__(self, file_path):
        file_directory = os.path.dirname(os.path.dirname(os.path.abspath(file_path)))
        file_name = os.path.basename(file_path)

        # Create a logger
        self.logger = logging.getLogger(file_name)
        self.logger.setLevel(logging.DEBUG)  # Set the logger level to DEBUG

        # Create a file handler
        file_handler = logging.FileHandler(f"{file_directory}\\test_outputs\\Logs\\logs_{file_name}.log", mode='w')
        file_handler.setLevel(logging.DEBUG)  # Set the file handler level to DEBUG

        # Create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)  # Set the console handler level to INFO

        # Create a formatter and add it to the handlers
        formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
