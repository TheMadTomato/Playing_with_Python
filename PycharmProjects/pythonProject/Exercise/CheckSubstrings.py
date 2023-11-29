"""
(Check substrings) You can check whether a string is a substring of another string
by using the find method in the str class. Write your own function to implement
find. Write a program that prompts the user to enter two strings and then checks
whether the first string is a substring of the second string.
"""

class CheckSubstrings:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def checkSubstrings(self):
        if self.s1 in self.s2:
            return f'{self.s1} is a substring of {self.s2}'
        else:
            return f'{self.s1} is not a substring of {self.s2}'

# test
s1 = input("enter the first string: ")
s2 = input("enter the second string: ")
sub = CheckSubstrings(s1, s2)
print(sub.checkSubstrings())