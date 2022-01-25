from .BaseStrategy import BaseStrategy
from web3 import w3
from eth_keys import keys
from envfile import *
import json

class DummyStrategy(BaseStrategy):
    def fetch_data(self):
        zesty = w3.eth.contract(
            address="0x9558c0d6daa769490b1310250718c846f9de7b8a", abi=EIP20_ABI)
        wallet = keys.PrivateKey(PRIVATE_KEY)
        nonce = w3.eth.get_transaction_count(wallet)
        get_price_txn = zesty.functions.getSellerAuctionPrice(
            '12').buildTransaction({
                'gas': 70000,
                'gasPrice': web3.toWei('1', 'gwei'),
                'from': wallet,
                'nonce': nonce
            })
        signed_txn = w3.eth.account.sign_transaction(get_price_txn, private_key=PRIVATE_KEY)
        value = w3.eth.send_raw_transaction(signed_txn.rawTransaction)  # doctest: +SKIP
        print(value)
        return value

    def process_data(self, raw_data):
        if self.get_price < raw_data.price_main:
            return True
        else:
            return False

    def act(self, processed_data):
        if processed_data:
            print("prcess")
            #call_bid_contract
        else:
            pass
        return {'dummy': 'dummy'}
