# Joseph Do
# Project 4 Sum of Digits in a String
# This program will give the sum of all single digit numbers in a string

def addNumber(number):

    # Initial total
    total = 0

    # Get each number individual, convert from string to int, add
    for n in number:
        n = int(n)
        total = n + total

    # Print result
    print("Total of all digit in number is:",total)
    
def main():

    # Prompt user input
    print("Enter a series of single digit numbers.")
    number = input("Number: ")

    # Check if number is valid
    while (number.isdigit() == False):
        print("Digits only.")
        number = input("Number: ")

    addNumber(number)

# Start program    
main()
