# Joseph Do
# Project 5
# Largest List Item
# This program will accept a list as an argument and return the largest value

def findLargest(data):

    # Return largest number
    if len(data) == 1:
        return data[0]

    # Use recursion
    largest = findLargest(data[0:-1])

    # Return if element is greatest
    if largest < data[-1]:
        return data[-1]
    else:
        return largest

def main():

    # Create list
    numberList = [1, 5, 9, 7, 3, 4, 8, 6, 2, 11]

    largestNumber = findLargest(numberList)

    # Display
    print("The largest value is:", largestNumber)

# Start program
main()
