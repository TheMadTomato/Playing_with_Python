#Enter your grades for this semester

x = int(input('Enter CSI201 grade:'))
y = int(input('Enter ENG201 grade:'))
z = int(input('Enter HMS301 grade:'))
w = int(input('Enter MGT210 grade:'))
t = (x + y + z + w) / 4



courses = {
    'CSI201': x,
    'ENG201': y,
    'HMS301': z,
    'MGT210': w,
    'Total': t
    
}


print(courses)

if 224.25 < t < 299:
    print('You Passed!')
elif t > 299:
    print('You Passed with Honor, Congrats!!')
elif t < 224.25:
    print('You failed, Tryharder!')
    