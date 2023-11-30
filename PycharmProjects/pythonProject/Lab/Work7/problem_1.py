"""
Problem 1: Classes/Objects
Part1: Create a class named Person, use the __init__() function to assign values for name and age:
Part2: Write a Python class named Student with two attributes: student_id, student_name. Add a new
attribute: student_class. Create a function to display all attributes and their values in the Student
class.
"""
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# part1
print("Part1: Create a class named Person, use the __init__() function to assign values for name and age:")
p1 = person("Patu", 36)
print(p1.name)

# part2
print("\nPart2: Write a Python class named Student with two attributes: student_id, student_name. Add a new attribute: student_class. Create a function to display all attributes and their values in the Student class.")
class student:
    def __init__(self, student_id, student_name, student_class=""):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display(self):
        print("Student ID: ", self.student_id)
        print("Student Name: ", self.student_name)
        print("Student Class: ", self.student_class)

s1 = student(12220605, "Paul", "ICT")


s1.display()
print(s1.__dict__)