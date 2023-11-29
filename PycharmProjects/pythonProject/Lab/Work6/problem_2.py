"""
Problem 2:
Difficulty level: EASY-NORMAL
One of the most important things to do in Natural Language Processing (NLP) is to be able to get the
frequency of each word (how frequent each word is). The frequency is used to understand the
context of a certain paragraph and check the kind of vocabulary used by the author; the words that
are easier to understand tend to have a higher frequency. According to doodleenglish “Recognizing
and being able to read high frequency words give children more confidence: if a child can already
recognize a quarter of the words in a text, they are more likely to want to keep reading.”
Write a Python script that takes a text as input from the user and then outputs the frequency per
word. To accomplish this task, you are required to implement the following functions:
•
Function 1 – “clean”, this method takes a string and replaces all non-alphanumeric characters
with a space and converts the text to a unified case (upper or lower). Returns a cleaned-up
version of the string.
•
Function 2 – “split”, this method takes a string and splits it into words by using the space
character as separator. Returns a list of words.
•
Function 3 – “frequency”, this method takes a list of words and counts the occurrence of each
word using a dictionary. Returns a dictionary containing each word and its occurrence.
•
Function 4 – “print_dict”, this method takes the dictionary and print out the words along with
their occurrences.
"""
def clean(string):
    # if character is not alphanumeric, replace it with a space
    string = string.lower()
    for i in range(len(string)):
        if not string[i].isalnum():
            string = string.replace(string[i], " ")
    return string

def split(string):
    # return string.split(" ")
    # f.e "hello world" -> ["hello", "world"]
    return string.split()

def frequency(words):
    # in a dictionary, key is the word and value is the frequency
    # if the occurence of a word is n, then the value is n
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def print_dict(freq):
    # using the .items() method, we can get the key and value of each item in the dictionary
    for key, value in freq.items():
        print(key, "->", value)

text = input("Enter a text: ")
text = clean(text)
words = split(text)
freq = frequency(words)
print_dict(freq)
