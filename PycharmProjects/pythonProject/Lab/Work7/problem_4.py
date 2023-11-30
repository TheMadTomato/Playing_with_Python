"""
Problem 4:
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

class nlp:
    def __init__(self, text):
        self.text = text
        self.freq = {}

    def clean(self):
        # if character is not alphanumeric, replace it with a space
        self.text = self.text.lower()
        for i in range(len(self.text)):
            if not self.text[i].isalnum():
                self.text = self.text.replace(self.text[i], " ")

    def split(self):
        # return string.split(" ")
        # f.e "hello world" -> ["hello", "world"]
        return self.text.split()

    def frequency(self):
        # in a dictionary, key is the word and value is the frequency
        # if the occurence of a word is n, then the value is n
        self.freq = {}
        for word in self.text:
            if word in self.freq:
                self.freq[word] += 1
            else:
                self.freq[word] = 1
        return self.freq

    def print_dict(self):
        # using the .items() method, we can get the key and value of each item in the dictionary
        for key, value in self.freq.items():
            print(key, "->", value)

text = input("Enter a text: ")
text = nlp(text)
text.clean()
text.split()
text.frequency()
text.print_dict()

