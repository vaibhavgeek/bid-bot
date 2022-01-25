DUMMY_QUERY = '''
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