
"""
(Compute e) You can approximate e by using the following series:

Write a program that displays the e value for i = 10000, 20000, . . ., and
100000.(Hint: Because i! = i * (i - 1) * ... * 2 * 1, then 1/i! is 1/(i(i - 1)!)
For example, 1/3! is 1/(3 * 2 * 1).)

initialize e = 1 and item = 1 and keep adding item to e. The new e is the previous item divided by i for
i = 2, 3, 4, . . . . In this case, e = 1 + 1/2! + 1/3! + 1/4! + ... + 1/i!
"""
e = 1
item = 1
for i in range(1, 100000 + 1):
    # the item's purpose is to store the previous item divided by i
    item = item / i
    # we add item to e because we want to keep adding the previous item divided by i to e
    e += item
    if i % 10000 == 0:
        print(f"e for i = {i} is {e}")