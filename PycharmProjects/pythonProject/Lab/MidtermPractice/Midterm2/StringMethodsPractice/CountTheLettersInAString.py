"""
(Count the letters in a string) Write a function that counts the number of letters in
a string using the following header:
def countLetters(s):
Write a test program that prompts the user to enter a string and displays the num-
ber of letters in the string.
"""
def countLetter(s):
    count = 0
    for i in s:
        if i.isalpha():
            count += 1
    return count

def main():
    s = input("Enter a string: ")
    print("The number of letters in", s, "is", countLetter(s))

main()