# Author: Luis Pringle
# GitHub username: PringleElUno
# Date: 11/18/2024
# Define a class named Employee that has private data members for an employees
# _name, _ID_number, _salary, and _email address.

# Define the class as employee
class Employee:
    """
    Class: Employee that has _name, _ID_number, _salary, and _email address.

    Attributes:
    _name (str): The name of the employee.
    _ID_number (str): The ID number of the employee.
    _salary (float): The salary of the employee.
    _email_address (str): the email address of the employee.

    Methods:
    get_name(): Returns the name of the employee.
    get_ID_number(): Returns the ID number of the employee.
    get_salary(): Returns the salary of the employee.
    get_email_address(): Returns the email address of the employee.
    """

    def __init__(self, name, ID_number, salary, email_address):
    # Initializing the private data members
        self._name = name
        self._ID_number = ID_number
        self._salary = salary
        self._email_address = email_address

    # Define the getter methods
    def get_name(self):
        return self._name

    def get_ID_number(self):
        return self._ID_number

    def get_salary(self):
        return self._salary

    def get_email_address(self):
        return self._email_address

# Define employee dictionary list
def make_employee_dict(names, ids, salaries, emails):
    """
    Creates a employee dictionary of objects from the lists of employee information.

    Parameters:
    names (lists of str): The list of employee names.
    ids (lists of str): The list of employee ID numbers.
    salaries (lists of float): The list of employee salaries.
    emails (list of str): The list of employee email addresses.
    """
    # Initialize an empty dictionary to store employee objects
    employee_dict = {}

    # Use a range to loop through the indices of the lists
    for index in range (len(names)):
        names = names[index]
        ID_number = ids[index]
        salary = salaries[index]
        email_address = emails[index]
        # Create the employee object for each set of values.
        employee = Employee(names, ID_number, salary, email_address)

        # Add the Employee object to the dictionary using [ID_number]
        employee_dict[ID_number] = employee

    # Return the dictionary
    return employee_dict
