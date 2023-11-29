"""
Problem 1: Hash code
Difficulty level: EASY
A hash code is a number that can represent the content of a certain object/data value. Hash codes are
usually used to identify a variable’s content, check for content equality, and assign an index for that
object. The purpose of hash code is to help in efficient lookup and insertion in data collections which
are based on a hash table.
Write a Python function named “get_hash_code” that generates a unique hash code for any given
string by using the following formula:
n−1
hc = ∑ ci × 31 (n−(i+1)) i=0
hc: The hash code
n: The length of the string
ci : The ASCII decimal code of the character at index i
To help you visualize and partially validate your work checkout this ASCII table website. Test cases:
get_hash_code(“HelloWorld”) →
 1992865264673280 get_hash_code(“hashme”) →
 3070542630
"""

def get_hash_code(string):
    hash_code = 0
    for i in range(len(string)):
        hash_code += ord(string[i]) * 31 ** (len(string) - (i + 1))
        #print(hash_code) uncomment to see the process
    return hash_code

print(get_hash_code("HelloWorld"))
print(get_hash_code("hashme"))

# methode 2 with enumerate
# def get_hash_code(string):
#     hash_code = 0
#     for i, c in enumerate(string):
#         hash_code += ord(c) * 31 ** (len(string) - (i + 1))
#     return hash_code
#
# print(get_hash_code("HelloWorld"))
# print(get_hash_code("hashme"))