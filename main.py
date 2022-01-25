import gql
import web3
import os
import envfile
import importlib
from strategies.DummyStrategy import DummyStrategy

class BidBot(object):
    def __init__(
        self, 
        strategy, 
        network="polygon",
        fetch_interval=600
    ):
        """
        Constructor

        Parameters
        __________
        strategy : str
            The name of strategy this should refer to the 
        private_key : str
            The private key of the operator
        network : str
            The name of the network used (default is polygon)
        fetch_interval : int
            The time to fetch and process data (default is 600 which is 10 minutes)
        """
        module = importlib.import_module("strategies." + strategy)
        classobj = getattr(module, strategy)
        self.strategy = classobj()
        self.private_key = envfile.PRIVATE_KEY
        self.network = network
        self.raw_data = None
        self.processed_data = None

    def fetch_data(self):
        """
        Fetch data using strategy defined
        """
        self.raw_data = self.strategy.fetch_data()

    def process_data(self):
        """
        Processes raw data using strategy defined
        """
        self.processed_data = self.strategy.process_data(self.raw_data)

    def act(self):
        """
        Makes a decision based on processed data and updates 
        processed data based on results
        """
        self.processed_data = self.strategy.act(self.processed_data)

    def run(self):
        """
        Runs the strategy
        """
        # TODO: this might need to be done asynchronously
        while True:
            try:
                abc = self.fetch_data()
                defa = self.process_data(abc)
                return self.act(defa)

            except Exception as e:
                print(e)

if __name__ == "__main__":
    bidbot = BidBot("DummyStrategy")
    bidbot.run()