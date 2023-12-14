"""
(Display the first days of each month) Write a program that prompts the user
to enter the year and first day of the year, and displays the first day of each month
in the year on the console. For example, if the user entered year 2013, and 2 for
Tuesday, January 1, 2013, your program should display the following output:
January 1, 2013 is Tuesday
...
December 1, 2013 is Sunday
"""
import calendar

year = eval(input("Enter the year: "))
firstDay = eval(input("Enter the first day of the year: "))

for month in range(1,12+1):
    print(calendar.month_name[month], "1,", year, "is", calendar.day_name[firstDay])
    firstDay = (firstDay + 1) % 7
    # print("firstDay is", firstDay)