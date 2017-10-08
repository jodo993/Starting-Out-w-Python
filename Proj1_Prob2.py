# Joseph Do
# Project 1 - Stock Transaction Program
# This program will calculate the stock options for Joe

# Constant variables, Joe's initial stock information
NUMBER_OF_SHARE = 2000
AMOUNT_PER_SHARE = 40

# Stockerbroker commission for both buy and sell
STOCKBROKER_COMMISSION = 0.03

# Joe's stock information for selling
NUMBER_OF_SOLD_SHARE = 2000
AMOUNT_SOLD_PER_SHARE = 42.75

# Calculating amount Joe paid for stock
stockAmountPaid = NUMBER_OF_SHARE * AMOUNT_PER_SHARE

# Amount commission Joe paid broker for stock
brokerCommissionBuy = stockAmountPaid * STOCKBROKER_COMMISSION

# Amount Joe sold the stock
stockAmountSold = NUMBER_OF_SOLD_SHARE * AMOUNT_SOLD_PER_SHARE

# Amount Joe paid broker for sold stock
brokerCommissionSold = stockAmountSold * STOCKBROKER_COMMISSION

# Total amount Joe paid stockbroker
totalBrokerFee = brokerCommissionBuy + brokerCommissionSold

# Amount of money Joe had left
amountLeftForJoe = stockAmountSold - totalBrokerFee

# Display result
print("Amount of money Joe paid for stock:    ","$%8.2f" % stockAmountPaid)
print("Amount commission broker got for buy:  ","$%8.2f" % brokerCommissionBuy)
print("Amount Joe sold the stock:             ","$%8.2f" % stockAmountSold)
print("Amount commission broker got for sold: ","$%8.2f" % brokerCommissionSold)
print("Amount of money leftover:              ","$%8.2f" % amountLeftForJoe,"(includes stock amount)")

# Joe's profit
profit = stockAmountSold - stockAmountPaid
profit = profit - totalBrokerFee
print("Joe made:                              ","$%8.2f" % profit,"profit.")

