


Person bid on space, 
    pricePending != 0 and priceEnd == 0 and buyerCampaignsPending == [true] and buyerCampaignsApproved == [false]
    
    seller can either reject or approve any bid. 
        -   if reject, buyerCampaignsPending = [false] and buyerCampaignsApproved = [false]
        you can bid on separate auction because it is rejected. 

        - if approve, buyerCampaignsPending = [false] and buyerCampaignsApproved = [true]
        you cannot bid on this auction (bidding is completed.)


1. Fetch data from thegraph using the above defined conditions and if the bid is open then get the id of all the open auctions. 

2. Get the price from 0x8645A4D5fB4816EDec2ae4B1B822B11260830043 on polygon chain and store it for comparision = PRICE

3. IF BIDDING_AMOUNT > PRICE = BID to the AUCTION GIVEN THAT ENOUGH FUNDS ARE AVAILABLE IN WALLET. 
   ELSE do nothing. 
      

{
    sellerAuctions(where: {auctionTimeEnd_gt: 1643053244, pricePendin , cancelled: false, buyerCampaignsPending: [true], 
    buyerCampaignsApproved_not_contains: [true]}){
    
    id
    seller
    cancelled
    priceStart
    priceEnd
    pricePending
    currency
    buyerCampaignsPending
    buyerCampaignsApproved
  }
}
