from audioop import add
from eth_keys import keys
from envfile import *
import json
import codecs
from web3 import Web3, HTTPProvider
import requests

w3 = Web3(HTTPProvider(RPC_POLYGON))
f = open("ABI/api.json")
EIP20_ABI = json.load(f)
nonce = 0


query = '''
{
  sellerAuctions(where: { priceEnd: 0, pricePending_gt: 0 , cancelled: false ,buyerCampaignsPending: [true], buyerCampaignsApproved_not_contains: [true]}){
    id,
    seller,
    cancelled,
    priceStart,
    priceEnd,
    pricePending,
    currency,
    buyerCampaignsPending,
    buyerCampaignsApproved
  }
}
'''

data = requests.post(GRAPH_POLYGON,"",json={"query": query})
#print(data.text)
auctions = json.loads(data.text)
auctions = auctions["data"]["sellerAuctions"]
for auction in auctions:
  print(auction["id"])
  zesty = w3.eth.contract(
      address="0x8645A4D5fB4816EDec2ae4B1B822B11260830043", abi=EIP20_ABI['result'])
  private_key_bytes = w3.toBytes(hexstr=PRIVATE_KEY)
  wallet = keys.PrivateKey(private_key_bytes)
  address = wallet.public_key.to_checksum_address()
  nonce = w3.eth.get_transaction_count(address)
  get_price_txn = zesty.functions.getSellerAuctionPrice(
      1055).call()

  print(get_price_txn)
  if get_price_txn > BIDDING_AMOUNT:
    get_price_txn_buy = zesty.functions.sellerAuctionBidBatch(
        1336, BUYER_CAMPAIGN_ID).buildTransaction({
            'gas': 70000,
            'gasPrice': w3.toWei('1', 'gwei'),
            'from': address,
            'nonce': nonce
        })
    signed_txn = w3.eth.account.sign_transaction(
        get_price_txn_buy, private_key=PRIVATE_KEY)
    print(signed_txn)
    value = w3.eth.send_raw_transaction(
        signed_txn.rawTransaction)
    print(value)
