# How many courses Have you taken this semseter

courses = []

n = int(input("Enter the number of classes that you are taking this semester:"))

# Insert the classes to the list
for i in range(0, n):
    c = input()
    
    courses.append(c)

print(courses)

