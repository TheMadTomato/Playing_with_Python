"""
Difficulty level: EASY
Write a Python script that analyzes a given text and expands the abbreviations found. Assume that
the given text doesn’t contain any punctuations and is in lower case.
Your script must handle the following abbreviations:
•
•
- LOL: Laugh out loud
- BTW: By the way
- TBH: To be honest
- GTG: Got to go
- BRB: Be right back
- TTYL: Talk to you later
- OMW: On my way
- NGL: Not gonna lie
Example:
•
•
Input: btw when i tried to call you yesterday i got a bit mad tbh because you said ttyl
Output: by the way i tried to call you yesterday i got a bit mad to be honest because you said
talk to you later
"""

def expand_abbreviations(text):
    # use the script from problem_3.py and problem_2.py they git the logic
    new_text = ''
    for word in text.split():
        if word == 'lol':
            new_text += 'laugh out loud '
        elif word == 'btw':
            new_text += 'by the way '
        elif word == 'tbh':
            new_text += 'to be honest '
        elif word == 'gtg':
            new_text += 'got to go '
        elif word == 'brb':
            new_text += 'be right back '
        elif word == 'ttyl':
            new_text += 'talk to you later '
        elif word == 'omw':
            new_text += 'on my way '
        elif word == 'ngl':
            new_text += 'not gonna lie '
        else:
            new_text += word + ' '

    return new_text

text = input("Enter a text: ")
print(expand_abbreviations(text))

# methode 2: using dictionary
def expand_abbreviations_withDict(text):
    # use the script from problem_3.py and problem_2.py they git the logic
    new_text = ''
    abbreviations = {
        'lol': 'laugh out loud',
        'btw': 'by the way',
        'tbh': 'to be honest',
        'gtg': 'got to go',
        'brb': 'be right back',
        'ttyl': 'talk to you later',
        'omw': 'on my way',
        'ngl': 'not gonna lie'
    }
    for word in text.split():
        if word in abbreviations:
            new_text += abbreviations[word] + ' '
        else:
            new_text += word + ' '

    return new_text

text_D = input("Enter a text: ")
print(expand_abbreviations_withDict(text_D))