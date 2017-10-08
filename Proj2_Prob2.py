# Joseph Do
# Project 2 Population
# This program predicts the approximate size of a population of organisms

def main():
    # Obtain inputs from user
    print("Enter the requested data below.")
    startingNumberOrganism = int(input("Starting number of organisms: "))
    averageDailyIncrease = int(input("Average daily increase: "))
    numberDaysMultiply = int(input("Number of days to multiply: "))

    # Convert daily increase to percentage, population to user input, day to 1
    averageDailyIncrease = averageDailyIncrease / 100
    population = startingNumberOrganism
    day = 1

    # Display heading and first day
    print("Day Approximate %20s" % "Population")
    print(day, "%25s" % population)

    # While within those days, update the day and population
    while (day < numberDaysMultiply):
        populationIncrease = startingNumberOrganism * averageDailyIncrease
        population = population + populationIncrease
        day = day + 1
        print("%-25s" % day, "%.3f" % population)
        startingNumberOrganism = population

# Start program
main()

# Not sure why book has 1-5 decimal places randomly for population
