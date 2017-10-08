# Joseph Do
# Project 1 - 6. Sales Tax
# This program will compute the sales tax and total sale

# Gather the amount of the purchase
amountOfPurchase = input("Please enter the amount of purchase: ")
amountOfPurchase = float(amountOfPurchase)

# Tax Rate
STATE_SALES_TAX = 0.05
COUNTY_SALES_TAX = 0.025

# Calculate each sales tax, total sales tax, and total overall
itemStateSalesTax = amountOfPurchase * STATE_SALES_TAX
itemCountySalesTax = amountOfPurchase * COUNTY_SALES_TAX
totalSalesTax = itemStateSalesTax + itemCountySalesTax
totalSales = totalSalesTax + amountOfPurchase

# Display Results
print("Amount of Purchase: ","$%.2f" % amountOfPurchase)
print("State Sales Tax:    ","$%.2f" % itemStateSalesTax)
print("County Sales Tax:   ","$%.2f" % itemCountySalesTax)
print("Total Sales Tax:    ","$%.2f" % totalSalesTax)
print("Total Sale:         ","$%.2f" % totalSales)
