"""
(Check password ) Some Web sites impose certain rules for passwords. Write a
function that checks whether a string is a valid password. Suppose the password
rules are as follows:
■ A password must have at least eight characters.
■ A password must consist of only letters and digits.
■ A password must contain at least two digits.
Write a program that prompts the user to enter a password and displays valid
password if the rules are followed or invalid password otherwise.
"""
import re

class CheckPassword:
    def __init__(self, password):
        self.password = password

    def checkPassword(self):
        # create regex pattern
        pattern = r'^[a-zA-Z0-9]{8,}$'
        # re.match methode match the input to the regex pattern while
        # re.search method search the input for the regex pattern inside it's argument
        # in this case to check if the input contains at least two digits
        # use the match() method to search pattern
        if re.match(pattern, self.password) and re.search(r'\d{2,}', self.password):
            return 'Valid Password'
        else:
            return 'Invalid Password'

# test
password = input("enter the password: ")
pw = CheckPassword(password)
print(pw.checkPassword())