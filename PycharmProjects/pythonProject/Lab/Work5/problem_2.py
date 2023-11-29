"""
Difficulty level: EASY-NORMAL
Write a function that takes in a list of integers and returns True if it contains 961 in order. Test cases:
has_961([1,2,4,9,6,1,5]) --> True has_961([1,9,2,4,6,5,1]) --> True
has_961([1,6,2,0,4,5,9]) --> False
"""


# method 1
def has_961(lst):
    for i in range(len(lst) - 2):
        if lst[i] == 9 and lst[i + 1] == 6 and lst[i + 2] == 1:
            return True
    return False


lst = [1, 2, 4, 9, 6, 1, 5]
print(has_961(lst))

lst = [1, 9, 2, 4, 6, 5, 1]
print(has_961(lst))


# method 2
# def has_961(lst):
#     return '961' in ''.join([str(i) for i in lst])
#
#
# print(has_961([1, 2, 4, 9, 6, 1, 5]))
# print(has_961([1, 9, 2, 4, 6, 5, 1]))



