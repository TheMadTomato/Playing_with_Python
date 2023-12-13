"""
(Check SSN) Write a program that prompts the user to enter a Social Security
number in the format ddd-dd-dddd, where d is a digit. The program displays
Valid SSN for a correct Social Security number or Invalid SSN otherwise.
"""

import re

class CheckSSN:
    def __init__(self, ssn):
        self.ssn = ssn

    def checkSSN(self):
        # create regex pattern
        pattern = r'^\d{3}-\d{2}-\d{4}$'
        # use the match() method to search pattern
        if re.match(pattern, self.ssn):
            return 'Valid SSN'
        else:
            return 'Invalid SSN'

# test
ssid = input("enter the ssn: ")
ssn = CheckSSN(ssid)
print(ssn.checkSSN())