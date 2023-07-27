#Enter the number of courses for this semester as inputs
courses = {}

n = int(input('ENTER YOUR COURSES COUNT FOR THIS SEMESTER: '))

print('\n')
#n number of courses will be updates to the ditionary where each class name will be assigned a grade
print("Enter your courses and grades: ")# Add the Course first and then Its grade
for i in range(0, n):
    c=input('Course: ')
    k=int(input('Grade: '))
    
    courses.update({c:k})
 
print(courses)
print("\n")
# this function calculates the average of the grade assigned to each course
def returnGPA(MyDict):

    L=[]
    for i in MyDict:
        L.append(MyDict[i])
    gpa = sum(L) / len(courses)

    return gpa 
x = returnGPA(courses)

print('Final GPA: ', x)
print('\n')
# this if loop will tell the user whether he passed or not
if 224.25 <= x < 299:
    print('You have passed this semester.')
elif x > 299:
    print('You did very well this semester, Congrats!!')
elif x < 224.25:
    print('You have failed semester, work harder next time!')

            