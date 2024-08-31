from abc import ABC, abstractmethod
import logging

class BaseAgent(ABC):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    @abstractmethod
    def process(self, input_data):
        pass

    def log(self, message):
        self.logger.info(message)