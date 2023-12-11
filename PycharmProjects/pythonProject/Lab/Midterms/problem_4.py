"""
Write a function that takes in a list of integers and returns True if it contains 961 in order.
Test cases:
has_961([1,2,4,9,6,1,5]) --> True has_961([1,9,2,4,6,5,1]) --> True
has_961([1,6,2,0,4,5,9]) --> False has_961([1,2,9,6,1,5]) --> False
"""
def has_961(list):
    for i in range(len(list)):
        if list[i] == 9 and list[i+1] == 6 and list[i+2] == 1:
            return True
    return False

# test
print(has_961([1,2,4,9,6,1,5]))
print(has_961([1,9,2,4,6,5,1]))