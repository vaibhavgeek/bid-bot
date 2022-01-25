from strategies.quries import DUMMY_QUERY
from .BaseStrategy import BaseStrategy
from eth_keys import keys
from envfile import *
import json
import codecs
from web3 import Web3, HTTPProvider
import requests
import quries

class DummyStrategy(BaseStrategy):
    w3 = Web3(HTTPProvider(RPC_POLYGON))
    f = open("ABI/api.json")
    EIP20_ABI = json.load(f)
    nonce = 0
    def fetch_data(self):
        data = requests.post(GRAPH_POLYGON,"",json={"query": DUMMY_QUERY})
        auctions = json.loads(data.text)
        auctions = auctions["data"]["sellerAuctions"]
        return auctions

    def process_data(self, auctions):
        biddings = []
        for auction in auctions:
            self.zesty = self.w3.eth.contract(
                address=POLYGON_CONTRACT_ADDRESS, abi=self.EIP20_ABI['result'])
            get_price_txn = self.zesty.functions.getSellerAuctionPrice(
                auction["id"]).call()
            if get_price_txn > BIDDING_AMOUNT:
                biddings.append(auction)


    def act(self, biddings):
        for bid in biddings:
            private_key_bytes = self.w3.toBytes(hexstr=PRIVATE_KEY)  
            wallet = keys.PrivateKey(private_key_bytes)
            address = wallet.public_key.to_checksum_address()
            nonce = self.w3.eth.get_transaction_count(address)
        
            get_price_txn_buy = self.zesty.functions.sellerAuctionBidBatch(
            bid["id"], BUYER_CAMPAIGN_ID).buildTransaction({
                'gas': 70000,
                'gasPrice': self.w3.toWei('1', 'gwei'),
                'from': address,
                'nonce': nonce
            })
            signed_txn = self.w3.eth.account.sign_transaction(
                get_price_txn_buy, private_key=PRIVATE_KEY)
            value = self.w3.eth.send_raw_transaction(
                signed_txn.rawTransaction)



## Flow for dummy strategy
# Person bid on space, 
#     pricePending != 0 and priceEnd == 0 and buyerCampaignsPending == [true] and buyerCampaignsApproved == [false]
    
#     seller can either reject or approve any bid. 
#         -   if reject, buyerCampaignsPending = [false] and buyerCampaignsApproved = [false]
#         you can bid on separate auction because it is rejected. 

#         - if approve, buyerCampaignsPending = [false] and buyerCampaignsApproved = [true]
#         you cannot bid on this auction (bidding is completed.)


# 1. Fetch data from thegraph using the above defined conditions and if the bid is open then get the id of all the open auctions. 

# 2. Get the price from 0x8645A4D5fB4816EDec2ae4B1B822B11260830043 on polygon chain and store it for comparision = PRICE

# 3. IF BIDDING_AMOUNT > PRICE = BID to the AUCTION GIVEN THAT ENOUGH FUNDS ARE AVAILABLE IN WALLET. 
#    ELSE do nothing. 
      

# {
#     sellerAuctions(where: {auctionTimeEnd_gt: 1643053244, pricePendin , cancelled: false, buyerCampaignsPending: [true], 
#     buyerCampaignsApproved_not_contains: [true]}){
    
#     id
#     seller
#     cancelled
#     priceStart
#     priceEnd
#     pricePending
#     currency
#     buyerCampaignsPending
#     buyerCampaignsApproved
#   }
# }
