"""
(Occurrences of a specified character) Write a function that finds the number of
occurrences of a specified character in a string using the following header:
def count(s, ch):
The str class has the count method. Implement your method without using the
count method. For example, count("Welcome", 'e') returns 2. Write a test
program that prompts the user to enter a string followed by a character and dis-
plays the number of occurrences of the character in the string.
"""

class OccurenceOfASpecifiedCharacter:
    def __init__(self, s, ch):
        self.s = s
        self.ch = ch

    def count(self):
        count = 0
        for i in self.s:
            if i == self.ch:
                count += 1
        return count


# test
s = input("enter the string: ")
ch = input("enter the character: ")
occ = OccurenceOfASpecifiedCharacter(s, ch)
print(occ.count())