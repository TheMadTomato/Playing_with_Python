"""
(Occurrences of a specified character) Write a function that finds the number of
occurrences of a specified character in a string using the following header:
def count(s, ch):
The str class has the count method. Implement your method without using the
count method. For example, count("Welcome", 'e') returns 2. Write a test
program that prompts the user to enter a string followed by a character and dis-
plays the number of occurrences of the character in the string.
"""
def count(s, ch):
    count = 0
    for i in s:
        if i == ch:
            count += 1
    return count

def main():
    s = input("Enter a string: ")
    ch = input("Enter a character: ")
    print("The number of occurrences of", ch, "in", s, "is", count(s, ch))

main()