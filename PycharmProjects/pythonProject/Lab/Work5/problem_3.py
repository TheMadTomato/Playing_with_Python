"""
Difficulty level: EASY
Write a Python function that takes a string and then returns a new string where for every lower-case
character in the original there are three characters.
Test cases:
spam_lc('Hello') --> 'Heeellllllooo'
spam_lc('Lebanon') --> 'Leeebbbaaannnooonnn'
"""

def spam_lc(string):
    new_string = ''
    for char in string:
        if char.islower():
            new_string += char*3
        else:
            new_string += char
    return new_string

print(spam_lc('Hello'))
print(spam_lc('Lebanon'))