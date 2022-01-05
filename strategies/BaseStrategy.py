from abc import ABC

class BaseStrategy(ABC):
    def fetch_data(self):
        pass

    def process_data(self, raw_data):
        pass

    def act(self, processed_data):
        pass