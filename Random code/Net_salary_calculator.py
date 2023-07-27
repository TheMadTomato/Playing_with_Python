h=int(input('Enter how many hours you have worked this week:'))
s=int(input('how much are you paid per hours:$'))
BS= s * h
OH= (h - 40) * s
if BS > 1000:
    print('Your Net Salary is: $', (BS + OH * 2) - (BS * 10/100))
elif 500 < BS < 1000:
    print('Your Net Salary is: $', (BS + OH * 2) - (BS * 5/100))
elif BS < 500:
    print('Your Net Salary is: $', (BS + OH * 2) - (BS * 5/100))