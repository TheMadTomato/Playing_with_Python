"""
Youtube Link: https://youtu.be/3ohzBxoFHAY?si=lFlXkQrqj-aPoSau

Special (Magic/Dunder) Methods

what are special methods and operators overloading?
    - special methods are methods that allow us to emulate some built in behavior within python and it is also how we
      implement operator overloading
    - operator overloading means that we can change the behavior of operators like +, -, * etc.
    - special methods are always surrounded by double underscores __init__ is an example of a special method
    - special methods are also called magic methods or dunder methods
    - we can use special methods to emulate built in behavior within python and operator overloading
    - we can use special methods to make our classes act like built in types
    - we can use special methods to make our classes iterable
    - we can use special methods to make our classes act like numeric types
    - we can use special methods to make our classes callable
    - A dunder is a double underscore __ and a duner method is a method surrounded by double underscores __init__ is an
        example of a dunder method
    - A magice method is a method that allows us to emulate some built in behavior within python
      f.e __len__ is a magic method that allows us to use the len function on our objects
    - A special method is a method that allows us to use operator overloading

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

    def __repr__(self):
        # this is a special method that will return a string that can be used to recreate the object
        # if __repr__ is not defined it will use __str__ instead
        # it is used for debugging and logging and meant to be seen by other developers
        return "employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        # this is a special method that will return a string that is readable
        # if __str__ is not defined it will use __repr__ instead
        # it is used to display information to the end user
        return '{} - {}'.format(self.fullname(), self.email)
    def __add__(self, other):
        # this is a special method that will change the behavior of the + operator
        # it will add the pay of 2 employees
        return self.pay + other.pay
    def __len__(self):
        # this is a special method that will change the behavior of the len function
        # it will return the length of the fullname of an employee
        return len(self.fullname())

emp_1 = employee("Corey", "Schafer", 50000)
emp_2 = employee("Yorick", "Joestar", 60000)

# repr(emp_1)
# str(emp_1)

# print(emp_1.__str__())
# print(emp_1.__repr__())

# there is arithmetic magic methods that we can use to change the behavior of operators like +, -, * etc.
# + = __add__(self, other)
# we can customize the behavior of the + operator by defining the __add__ method
# print(1+2)
# print(int.__add__(1,2))

print(emp_1 + emp_2)

# we changed the properties of len function by defining the __len__ dunder method in the class
print(len(emp_1))

"""
returning NotImplemented is a way to tell python to handle the operation itself and not to return an error, to see if 
another object can handle the operation
"""