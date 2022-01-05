from .BaseStrategy import BaseStrategy

class DummyStrategy(BaseStrategy):
    def fetch_data(self):
        print("fetch")
        pass

    def process_data(self, raw_data):
        print('process')
        return {'dummy': 'dummy'}

    def act(self, processed_data):
        print("act")
        return {'dummy': 'dummy'}