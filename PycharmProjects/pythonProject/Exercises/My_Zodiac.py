# Chinese zodiac sign
year = eval(input("Enter the year you were born in: "))

zodiacSign = year % 12
if zodiacSign == 0:
    print("Monkey")
elif zodiacSign == 1:
    print("Rooster")
elif zodiacSign == 2:
    print("Dog")
elif zodiacSign == 3:
    print("Pig")
elif zodiacSign == 4:
    print("Rat")
elif zodiacSign == 5:
    print("Ox")
elif zodiacSign == 6:
    print("Tiger")
elif zodiacSign == 7:
    print("Rabbit")
elif zodiacSign == 8:
    print("Dragon")
elif zodiacSign == 9:
    print("Snake")
elif zodiacSign == 10:
    print("Horse")
else:
    print("Sheep")
