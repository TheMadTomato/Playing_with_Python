"""
Youtube Link: https://youtu.be/RSl87lqOXDE?si=JxguUVeCHZn5zyeB

Inheritance and Creating Subclasses

What is inheritance?
    - inheritance is a way to form new classes using classes that have already been defined
    - the newly formed classes are called derived classes, the classes that we derive from are called base classes
    - important benefits of inheritance are code reuse and reduction of complexity of a program

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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class developper(employee): # this is a subclass of the class employee we inherited all the attributes and methods of
# the class employee and we can add more attributes and methods to the subclass
    raise_amount = 1.10 # this is a class variable that is different from the class variable of the class employee
    # to add a new attribute to the subclass we can use the init method
    def __init__(self, first, last, pay, prog_lang):
        # we can use the init method of the class employee to add the first, last and pay attributes
        super().__init__(first, last, pay) # this will run the init method of the class employee
        #employee.__init__(self, first, last, pay) # this will also run the init method of the class employee
        # we can also use the init method of the subclass to add the prog_lang attribute
        self.prog_lang = prog_lang

class manager(employee): # this is a subclass of the class employee
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_employees(self):
        for emp in self.employees:
            print("-->", emp.fullname())

# it will have the same output as employee objects because it inherited all the attributes and methods of the class employee
dev_1 = developper("Corey", "Schafer", 50000, "java")
dev_2 = developper("Yorick", "Joestar", 60000, "python")

mgr_1 = manager("Sue", "Smith", 90000, [dev_1])
print(mgr_1.email)

mgr_1.add_employee(dev_2)
mgr_1.remove_employee(dev_1)
mgr_1.print_employees()

# how to check if an object is an instaance of a class
print(isinstance(mgr_1, developper))
print(isinstance(mgr_1, manager))
# how to check if a class is a subclass of another class
print(issubclass(manager, employee))

# print(help(developper)) # this will print all the info about the class developper
# print(dir(developper)) # this will print all the attributes and methods of the class developper
# print(dev_2.prog_lang)
# print(dev_1.email)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

