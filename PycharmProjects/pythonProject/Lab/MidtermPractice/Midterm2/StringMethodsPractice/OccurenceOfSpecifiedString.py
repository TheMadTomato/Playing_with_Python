"""
(Occurrences of a specified string) Write a function that counts the occurrences of a
specified non-overlapping string s2 in another string s1 using the following header:
def count(s1, s2):
For example, count("system error, syntax error", "error") returns
2. Write a test program that prompts the user to enter two strings and displays the
number of occurrences of the second string in the first string.
"""
def count(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i:i+len(s2)] == s2:
            count += 1
    return count

def main():
    s1 = input("Enter string 1: ")
    s2 = input("Enter string 2: ")
    print("The number of occurrences of", s2, "in", s1, "is", count(s1, s2))

main()