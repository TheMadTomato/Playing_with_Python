"""
Write a Python script that accepts a string and calculates the number of upper-case letters, lower-case
letters, and digits. Use functions to organize your code. The code should be able to check whether the input
is a panagram or not. A panagram is a sentence that contains all the letters of the English alphabet at least.
Sample String: 'The quick Brown Fox jumps over the Lazy Dog'
Sample String: 'Hello Students, how was Exam 1 last Wednesday?'
"""


def is_panagram(string):
    # initializing the alphabet list
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # initializing the panagram list
    panagram = list()
    # initializing the counter
    count = 0
    # converting the string to lower case
    string = string.lower()
    # looping through the alphabet list
    for i in alphabet:
        # checking if the alphabet is in the string
        if i in string:
            # if the alphabet is in the string then add it to the panagram list
            panagram.append(i)
            # increase the counter by 1
            count += 1
    # checking if the counter is 26 which is the number of the alphabet
    if count == 26:
        # if the counter is 26 then return True
        return True
    else:
        # if the counter is not 26 then return False
        return False


# Take input sentence from the user
sentence = input("Pleas Enter a Text: ")
if is_panagram(sentence):
    print("The sentence is a panagram!")
else:
    print("The sentence is not a panagram!")
