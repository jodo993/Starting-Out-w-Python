# Employee Class and Shift Supervisor subclass

class Employee:

    # Initialize
    def __init__(self, name, idNumber):
        self.__name = name
        self.__id = idNumber

    # Set and get data for name and id number
    def set_name(self, name):
        self.__name = name

    def set_id(self, idNumber):
        self.__id = idNumber

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

class ShiftSupervisor(Employee):

    # Initialize
    def __init__(self, name, idNumber, salary, bonus):
        # Call the superclass to get the data
        Employee.__init__(self, name, idNumber)
        # Initialize the new data
        self.__salary = salary
        self.__bonus = bonus

    # Set and get data for salary and bonus
    def set_salary(self, salary):
        self.__salary = salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_salary(self):
        return self.__salary

    def get_bonus(self):
        return self.__bonus
        
