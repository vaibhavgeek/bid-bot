DUMMY_QUERY = '''
{
  sellerAuctions(where: { auctionTimeStart_lt:1643127004, auctionTimeEnd_gt  : 1643127004, cancelled: false , buyerCampaignsApproved_not_contains: [true]}){
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