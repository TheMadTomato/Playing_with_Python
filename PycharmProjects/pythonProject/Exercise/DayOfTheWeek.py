"""
You receive a date and need to know what day of the week it is.

Task:
Create a program that takes in a string containing a date, and outputs the day of the week.

Input Format:
A string containing a date in either "MM/DD/YYYY" format or "Month Day, Year" format.

Output Format:
A string containing the day of the week from the provided date.

Sample Input:
11/19/2019

Sample Output:
Tuesday
"""
import datetime

#input date in format MM/DD/YYYY or Month Day, Year
while True:
    try:
        date = input("Enter date: ")
        date = datetime.datetime.strptime(date, '%m/%d/%Y')
        break
    except ValueError:
        try:
            date = datetime.datetime.strptime(date, '%B %d, %Y')
            break
        except ValueError:
            print("Incorrect format")

#output day of the week
print(date.strftime("%A"))