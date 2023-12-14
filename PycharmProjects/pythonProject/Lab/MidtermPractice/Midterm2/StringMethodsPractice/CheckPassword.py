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
def isValidPassword(password):
    # A password must have at least eight characters.
    if len(password) < 8:
        return False
    else:
        # A password must consist of only letters and digits.
        for i in password:
            if i.isalpha() or i.isdigit():
                continue
            else:
                return False
        # A password must contain at least two digits.
        count = 0
        for i in password:
            if i.isdigit():
                count += 1
        if count >= 2:
            return True
        else:
            return False

def main():
    password = input("Enter a password: ")
    if isValidPassword(password):
        print("Valid password")
    else:
        print("Invalid password")

main()