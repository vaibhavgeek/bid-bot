# Bid Bot
Bid Bot is an auto-bidding bot for advertisers. 

## Motivations
It is very troublesome to bid on Zesty Market. 
Most advertisers are used to putting forth an advertising budget and getting a report on their campaigns.
Currently, the process of advertising bidding on Zesty Market is manual which can make it really troublesome.
The goal of Bid Bot is to make this process simple.

## Proposed Flows
### Layered on Zesty Market (For non-hackers)
1. Bid Bot is an extension off the Zesty Market App at app.zesty.market, this could be managed using Bob the Bot.

2. Advertisers create a campaign on Zesty Market as usual on `/campaigns`.

3. After creating a campaign, a prompt shows up to ask the advertiser wants to automate the campaigns

4. If no, the advertiser can bid as per usual. If yes, the advertiser goes on the next page to select parameters.

5. The parameter page should show the option to target webxr or twitch and pick the kind of demographic they are looking for.
After which the advertiser can set a budget and duration of the campaign to get the estimated impressions and clicks for the budget and time.

6. The advertiser clicks confirm and sees a review page asking them to check the final details. 

7. The advertiser will now need to approve an EOA managed by Bob the Bot, and send funds to that EOA according to the budget specified earlier.
If the bot is not funded within 20 mins, the campaign is cancelled. 

8. On the `campaigns` page the advertiser is able to see which campaigns is managed by a bot with some flag or indicator on that space. 
Clicking on the particular campaign, brings the advertiser to the campaign page.

9. On the campaign page, the advertiser will be able to see the campaigns that were bidded on and their status (awaiting approval, approved, active).
They should be able to see the funds left in their campaign budget, impressions obtained, and clicks obtained. 
The advertiser should be able to pause bidding or terminate an automated campaign and retrieve remaining funds.

10. An administrative fee will be collected at the end of an automated campaign (either through termination, or successful completion).
This is to help fund the maintenance of the bot and the gas used for making transactions on behalf of the advertiser.

### Standalone Bot (For hackers and the purpose of this repo)
1. The standalone version is designed for hackers to implement bidding strategies for advertisers. 
People can create their own services on top of Zesty Market and charge a fee for usage.

2. This will be a node program which will get data from thegraph and bid accordingly via an EOA. 
This EOA should be treated as hot storage as it will be need to be hosted on some server or computer actively connected to the internet.

3. This repo should host various bidding strategies for people to play with.
