# Save the CSV output of the previous problem onto a file named “grades.csv”.
import csv
# initialize the variables and lists
id_list = list()
name_list = list()
grade_list = list()
counter = 0
header = ['ID', 'Name', 'Grade']

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

# Open the file in write mode
open_file = open('./grades.csv', 'w')
writer = csv.writer(open_file)

writer.writerow(header)

for col in range(len(id_list)):
    data = [id_list[col], name_list[col], grade_list[col]]
    writer.writerow(data)




