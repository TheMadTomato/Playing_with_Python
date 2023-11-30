"""
Youtube Link: https://youtu.be/rq8cL2XMM5M?si=YhoDBOL3iBl3eKe7

Class Methods and Static Methods

what is the difference between a regular method, a class method and a static method?
    - regular methods in a class automatically take the instance as the first argument. By convention we call it self.
    - class methods take the class as the first argument. By convention we call it cls.
    - static methods don't pass anything automatically. They behave just like regular functions but we include them in
         our classes because they have some logical connection with the class.
    - we should use regular methods if we want to work with instances of a class
    - we should use class methods if we want to work with the class itself and the class variables
    - we should use static methods if we don't want to work with the instance or the class
"""


class employee:
    raise_amount = 1.04
    number_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        employee.number_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * employee.raise_amount)

    @classmethod  # this is a decorator that will change the method to a class method
    # class methods can be used as alternative constructors
    def set_raise_amount(cls, amount):  # cls is the class itself. we will work with the class instead of the instance
        cls.raise_amount = amount
    @classmethod
    def from_string(cls, emp_str): # this is an alternative constructor that will take a string and create an instance
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay) # this will return an instance of the class employee
        # in this way we parse the string and create an new object from it.
    @staticmethod # this is a decorator that will change the method to a static method
    def is_workday(day): # this is a static method that will check if the day is a workday or not
        # this method does not take the class or the instance as an argument
        if day.weekday() == 5 or day.weekday() == 6:
            # in python monday is 0 and sunday is 6
            return False
        return True

emp_1 = employee("Corey", "Schafer", 50000)
emp_2 = employee("Yorick", "Joestar", 60000)
"""
# before we use the set_raise_amount class method
print(employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# after we use the set_raise_amount class method
employee.set_raise_amount(1.05)  # this will change the raise_amount of the class employee to 1.05
# it is kinda close to emp_1.raise_amount = 1.05 but it is not the same
# because the class variable is changed not the instance variable
# running this method from an instance will also change the class variable because
# the first argument in the method is cls which is the class itself
print(employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
"""
"""
# example of using class methods as alternative constructors
# we will use a string to create an instance of the class employee
# the string will be in the format of first-last-pay
# we will use the class method split to split the string into a list
emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

# first, last, pay = emp_str_1.split("-")  # this will split the string into a list
# we can assign this line of code to a class method constructor

# new_emp_1 = employee(first, last, pay)  # this will create an instance of the class employee
new_emp_1 = employee.from_string(emp_str_1) # this will create an instance of the class employee
print(new_emp_1.email)
print(new_emp_1.pay)
"""

# example of using static methods
import datetime
my_date = datetime.date(2021, 7, 10)

print(employee.is_workday(my_date)) # this will return false because it is a weekend
