"""
Youtube Link: https://www.youtube.com/watch?v=ZDa-Z5JzLYM

Classes and Instances

why should we use classes?
    - classes allow us to logically group our data and functions in a way that is easy to reuse and also easy to build
      upon if need be.
    - classes are like a blueprint for creating instances
    - instances are objects created from a class f.e we can create a class called employee and then create instances of
      that class that represent specific employees. Each instance of the class can have attributes associated with it.
    - attributes are like variables that belong to a class/instance
    - methods are functions that we can define inside of a class. They are used to perform operations that sometimes
      utilize the attributes of the class/instance we created.
    - classes are a way to bring data and functionality together
"""

class employee: # this is a class
    def __init__(self, first, last, pay): # this is a constructor
        # add attributes to the class. instance attributes will be set automatically when we create instances
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

    def fullname(self): # this is a method. if self is missing error will happens
        return '{} {}'.format(self.first, self.last)

"""
emp_1 = employee() # this is an instance of the class employee
emp_2 = employee() # this is a different instance of the class employee

# print instances
print(emp_1)
print(emp_2)
"""

"""
# manually add attributes to the instances
emp_1.first = "Corey"
emp_1.last = "Schafer"
emp_1.email = "Corey.Schafer@company.com"
emp_1.pay = 50000

emp_2.first = "Yorick"
emp_2.last = "Joestar"
emp_2.email = "Yorick.Star@company.com"
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)
"""

# create instances of the class employee where init will run automatically
emp_1 = employee("Corey", "Schafer", 50000)
emp_2 = employee("Yorick", "Joestar", 60000)

employee.fullname(emp_1) # run instance manually

print(emp_1.email)
print(emp_2.email)

print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_2.fullname()) # this is the same as the line above
print(emp_2.fullname) # lack of parenthesis will return the method itself

