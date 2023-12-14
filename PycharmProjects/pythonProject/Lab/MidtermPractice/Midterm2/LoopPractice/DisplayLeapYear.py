"""
(Display leap years) Write a program that displays, ten per line, all the leap years
in the twenty-first century (from year 2001 to 2100). The years are separated by
exactly one space.
"""
def isLeapYear(year: int) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def main():
    count = 0
    for i in range(2001, 2101):
        if isLeapYear(i):
            count += 1
            print(i, end=" ")
            if count % 10 == 0:
                print()

main()