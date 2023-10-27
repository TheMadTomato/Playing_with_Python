"""
Write a Python script that will take the students’ information and print it in a CSV format.
For each student, the user must input the: ID (string), Name (string), and Grade (int). The script will
keep on taking students till -1 is entered as an ID. At the end, the script must output all information to
the console in a CSV format. The first line in a CSV text/file is usually the header which defines the
column names.
“A Comma Separated Values (CSV) format is a plain text format that contains a list of data. CSVs are
usually stored in files; these files are often used for exchanging data between different applications.
For example, databases and contact managers often support CSV files.”
As mentioned in the quote above, the data must be comma separated. Example: 12120077, John Doe,
76
Note: In this problem we will not save the CSV data onto a file. We’ll just print it to the console.

The first line “ID, Name, Grade” is the header which defines the name of each column. The first
column is the ID, the second column is the Name, the third column is the student’s grade.

"""
from os import system

# initialize the variables and lists
id_list = list()
name_list = list()
grade_list = list()
counter = 0
# Main loop
while True:
    counter += 1
    # Take input from the user
    print(f"Student [{counter}]: ")
    ID = int(input("\t- Enter ID: "))
    # Check if the ID is -1 then break the loop
    if ID == -1:
        break
    else:
        # Take input from the user
        name = input("\t- Enter Name: ")
        grade = int(input("\t- Enter Grade: "))
        # Append the input to the lists
        id_list.append(ID)
        name_list.append(name)
        grade_list.append(grade)

# Clear the screen
system("clear") # For Linux
# system("cls") # For Windows

# Display the header
print("ID, Name, Grade")
# Display the data in CSV format
for i in range(len(id_list)):
    print(f"{id_list[i]}, {name_list[i]}, {grade_list[i]}")




