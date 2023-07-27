 #part 1 of the code: input the courses that i have in a dictionary
courses = []

n = int(input('ENTER YOUR COURSES COUNT FOR THIS SEMESTER: '))

print('\n')

print("Enter your courses: ")

for i in range(0, n):
    c=input()
    
    courses.append(c)
    
print(courses)

print('\n')
#part 2 of the code is to enter courses' grades and output the final grade
gpa = 0
x = len(courses)
i = 1

print('\n')

print('Enter your grades: ')

while x != 0:#note for part 2 this is a temperoy solution the main goal is to assigne the input of the grades to each course
    g=int(input())
    
    gpa += g
    i += 1
    x -= 1
GPA = gpa/n

print('\n')

print('Your final GPA is: ', GPA)

print('\n')
#part 3 of this code outputs whether i passed or not 
if GPA >= 224.25:
    print('You have passed this semester.')
elif GPA > 299:
    print('You did very well this semester, Congrats!!')
elif GPA < 224.25:
    print('You have failed semester, work harder next time!')
    
#part 4 should output my highest grade and in which class and the lowest in which class
    