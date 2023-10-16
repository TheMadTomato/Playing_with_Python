'''
Write a python program to print the calendar of a given month and year “ .
Using ‘calendar’ module.
- Let the user to enter the month and year
'''

import calendar

month = eval(input("Enter the month: "))
year = eval(input("Enter the year: "))

print(calendar.month(year, month))
