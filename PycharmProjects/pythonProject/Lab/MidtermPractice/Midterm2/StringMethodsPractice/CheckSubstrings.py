"""
(Check substrings) You can check whether a string is a substring of another string
by using the find method in the str class. Write your own function to implement
find. Write a program that prompts the user to enter two strings and then checks
whether the first string is a substring of the second string.
"""
def isSubsting(s1, s2):
    if s1 in s2:
        return True
    else:
        return False

def main():
    s1 = input("Enter string 1: ")
    s2 = input("Enter string 2: ")
    if isSubsting(s1, s2):
        print(s1, "is a substring of", s2)
    else:
        print(s1, "is not a substring of", s2)

main()