DUMMY_QUERY = '''
{
  sellerAuctions(where: { auctionTimeStart_lt: {time}, auctionTimeEnd_gt  : {time}, cancelled: false , buyerCampaignsApproved_not_contains: [true]}){
    id,
    seller,
    cancelled,
    priceStart,
    priceEnd,
    pricePending,
    currency,
    buyerCampaignsPending,
    buyerCampaignsApproved,
    sellerNFTSetting {
      id
      tokenData {
        id
        uri
      }
    }
  }
}
'''