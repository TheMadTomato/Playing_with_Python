"""
Youtube Link: https://youtu.be/jCzT9XFZ5bw?si=QBI_1Fpt_2uv_0Ci

Property Decorators - Getters, Setters and Deleters

what are property decorators? Getters, Setters and Deleters?


"""

class employee:
    raise_amount = 1.04
    number_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        #self.email = first + "." + last + "@company.com"

        employee.number_of_employees += 1
    @property # this is a decorator that will change the method to a property
    def email(self):
        # this work the same as our email attribute but it is a method not an attribute
        # so we can use it as an attribute
        return '{}.{}@company.com'.format(self.first, self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    @fullname.setter # this is a decorator that will change the method to a setter
    def fullname(self, name):
        # this will set the first and last name of an employee
        first, last = name.split(" ")
        self.first = first
        self.last = last
    @fullname.deleter # this is a decorator that will change the method to a deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

emp_1 = employee("Corey", "Schafer", 50000)
#emp_1.first = "Jim" # this will change the first name of emp_1 to Jim but the email will not change
#emp_1.fullname = "Rami Abadir" # this will give an error cause we can't set an attribute that is a property
print(emp_1.first)
#print(emp_1.email()) # we added () cause it is a method now
#after a i made a setter lets try
emp_1.fullname = "Rami Abadir"
# to use email as an attribute we can use property decorators
print(emp_1.email) # now we can use email as an attribute
print(emp_1.fullname)

del emp_1.fullname # this will delete the fullname of emp_1