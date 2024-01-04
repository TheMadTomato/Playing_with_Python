"""
Problem 1 – Primitive Students Information System

Write a Python script that will allow the user to enter the information about multiple students. The
student’s information consists of:
• ID
• Name
• Exam 1 grade
• Exam 2 grade
• Exam 3 grade
The script will keep on asking the user for input till -1 is entered as an ID. The students’
information is to be stored within a dictionary. Then the program will display the following
menu:
1. Search and print a student’s information. (Search for a student based on the ID and
display the information)
2. Display all students. (Print all students)
3. Print failing students grouped by each exam. (Print the failed student’s ID,
name, and grade per exam)
4. Exit. (This will exit the user from the script :) )
HINT: The students must be stored in a dictionary where the ID is the key, and the rest of the
information is considered the value.
HINT 2: You can use a dictionary to be the value of a certain key within another dictionary. In other
words, you can have a dictionary within a dictionary.
"""
class Students:
    def __init__(self):
        # Initialize students dictionary it will be used as a nested dictionary
        self.students = {}

    def add_student(self, id, name, exam1, exam2, exam3):
        # This method works by adding a new key to the dictionary. 
        # The key is the student's ID and the value is a dictionary containing the student's information
        self.students[id] = {'name': name, 'exam1': exam1, 'exam2': exam2, 'exam3': exam3}

    def search_student(self, id):
        # This method works by searching the dictionary for the student's ID.
        if id in self.students:
            return self.students[id]
        else:
            return None
    
    def print_all(self):
        # This method works by looping through the dictionary and printing each student's information
        # the for syntax used here "id, student" is called tuple unpacking. It is used to loop through a dictionary
        # and get the key and value at the same time
        for id, student in self.students.items():
            print(f"ID: {id}")
            print(f"Name: {student['name']}")
            print(f"Exam 1: {student['exam1']}")
            print(f"Exam 2: {student['exam2']}")
            print(f"Exam 3: {student['exam3']}")
            print()

    def print_failing(self):
    
        for id, student in self.students.items():
            if student['exam1'] < 60:
                print(f"ID: {id}")
                print(f"Name: {student['name']}")
                print(f"Exam 1: {student['exam1']}")
                print()
            if student['exam2'] < 60:
                print(f"ID: {id}")
                print(f"Name: {student['name']}")
                print(f"Exam 2: {student['exam2']}")
                print()
            if student['exam3'] < 60:
                print(f"ID: {id}")
                print(f"Name: {student['name']}")
                print(f"Exam 3: {student['exam3']}")
                print()

def main():
    students = Students()
    # Loop to get student information
    while True:
        id = int(input("Enter ID or -1 to Exit: "))
        if id == -1:
            break
        name = input("Enter name: ")
        # exam1 = int(input("Enter exam 1 grade: "))
        # exam2 = int(input("Enter exam 2 grade: "))
        # exam3 = int(input("Enter exam 3 grade: "))
        # An alternatie method with for loop
        exams = []
        for i in range(3):
            exam = int(input(f"Enter exam {i+1} grade: "))
            exams.append(exam)
        students.add_student(id, name, exams[0], exams[1], exams[2])
       # students.add_student(id, name, exam1, exam2, exam3)
    # Loop to display menu
    while True:
        print("1. Search and print a student’s information.")
        print("2. Display all students.")
        print("3. Print failing students grouped by each exam.")
        print("4. Exit.")
        choice = int(input("Enter choice: "))
        if choice == 1:
            id = int(input("Enter ID: "))
            student = students.search_student(id)
            if student:
                print(f"ID: {id}")
                print(f"Name: {student['name']}")
                print(f"Exam 1: {student['exam1']}")
                print(f"Exam 2: {student['exam2']}")
                print(f"Exam 3: {student['exam3']}")
                print()
            else:
                print("Student not found")
        elif choice == 2:
            students.print_all()
        elif choice == 3:
            students.print_failing()
        elif choice == 4:
            break
        else:
            print("Invalid choice")

main()