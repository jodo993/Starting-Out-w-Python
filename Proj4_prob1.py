# Joseph Do
# Project 4 Expense Pie Chart
# This program read data from a file and plot a pie chart from it

import matplotlib.pyplot as plt

def main():

    # Create empty list
    category = []
    expense = []

    # Open file
    infile = open('Expenses.txt','r')

    # Add column to correct list
    for row in infile:
        row = row.split(',')
        category.append((row[0]))
        expense.append((row[1].rstrip('\n')))
    print(category)
    print(expense)

    
    # Create chart
    plt.pie(expense, labels=category)
    
    # Add title
    plt.title("Category and Expenses for Last Month")

    # Show pie chart
    plt.show()

# Start program
main()
