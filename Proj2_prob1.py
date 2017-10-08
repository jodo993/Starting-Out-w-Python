# Joseph Do
# Project 2 Shipping Charges
# This program will find the shipping charges of a package based on weight

TWO_LBS_LESS = 1.50     # 2 Pounds or Less Charge
TWO_TO_SIX = 3.00       # Over 2 but not more than 6
SIX_TO_TEN = 4.00       # Over 6 but not more than 10
OVER_TEN = 4.75         # Over 10

def main():
    # Ask user for weight
    print("Enter weight of package to find shipping price.")
    weightOfPackage = float(input("Weight: "))

    # Check to see if weight is higher than 0
    while (weightOfPackage < 0):
        print("Enter weight of package to find shipping price.")
        weightOfPackage = float(input("Weight: "))

    # Determine correct pricing
    if (weightOfPackage <= 2):
        shippingCharge = TWO_LBS_LESS
    elif (weightOfPackage > 2 and weightOfPackage <= 6):
        shippingCharge = TWO_TO_SIX
    elif (weightOfPackage > 6 and weightOfPackage <= 10):
        shippingCharge = SIX_TO_TEN
    elif (weightOfPackage > 10):
        shippingCharge = OVER_TEN
    else:
        print("Enter a valid number.")

    # Display result
    print("Shipping Charge:","$%.2f" % shippingCharge)

    choice()

def choice():
    # Ask if user would like to repeat
    choice = input("To weight again press Y.")
    
    if (choice == "Y"):
        main()
    else:
        print("Have a nice day!")
        
# Start program    
main()
