"""
Youtube Link: https://youtu.be/BJ-VvGyQxho?si=65bkY-uWLiUh-fOK

Class Variables

what are class variables?
    - class variables are variables that are shared among all instances of a class
      while instance variables can be unique for each instance like name, email, pay etc.
    - class variables should be the same for each instance of a class
    - class variables can be accessed using the class itself or an instance of the class

"""
class employee:

    raise_amount = 1.04 # this is a class variable
    number_of_employees = 0 # this is a class variable that increments by 1 every time an instance is created
    def __init__(self, first, last, pay):
        # variables or attriubtes of an instance
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "."+ last + "@company.com"

        # since inint is run every time an instance is created we can increment the number_of_employees by 1
        # every time an instance is created. but it would not make sense to call is as an instance variable
        # so we call it as a class variable
        employee.number_of_employees += 1
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * employee.raise_amount) # here the 1.04 is a locked variable i can't change it to change it i can make
                                        # it a class variable that can be changed. it cn be changed by the class itself
                                        # or an instance of the class.

emp_1 = employee("Corey", "Schafer", 50000)
emp_2 = employee("Yorick", "Joestar", 60000)

"""
# check how apply_raise works
print(emp_1.pay)
emp_1.apply_raise() # the pay of emp_1 will be increased by 4%
print(emp_1.pay)
"""

"""
# check how class variables work
print(employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# to access all info about the class or an instance we can use the following
print(emp_1.__dict__) # this will print all the attributes of the instance emp_1
print(employee.__dict__) # this will print all the attributes of the class employee

# We can also change the class variable in a instance without changing the class variable itself
emp_1.raise_amount = 1.05 # this will change the raise_amount of emp_1 to 1.05 but will not change the class variable
print(emp_1.__dict__) # this will print all the attributes of the instance emp_1
"""
print(employee.number_of_employees)