# Joseph Do
# Project 5
# Shift Supervisor Class
# This program will

import employee

def main():

    # Create an employee object, a shift supervisor object
    supervisor = employee.ShiftSupervisor("John", "1", 50000, 1000)

    # Display employee data
    print("Employee Data - ")
    print("Name:", supervisor.get_name())
    print("ID:", supervisor.get_id())
    print("Salary:", supervisor.get_salary())
    print("Bonus:", supervisor.get_bonus())

# Start the program
main()
