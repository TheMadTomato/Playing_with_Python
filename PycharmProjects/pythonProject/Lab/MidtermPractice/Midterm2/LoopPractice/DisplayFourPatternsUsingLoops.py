"""
(Display four patterns using loops) Use nested loops that display the following
patterns in four separate programs:
Pattern A     Pattern B         Pattern C       Pattern D
1             1 2 3 4 5 6               1     1 2 3 4 5 6
1 2           1 2 3 4 5               2 1     1 2 3 4 5
1 2 3         1 2 3 4               3 2 1     1 2 3 4
1 2 3 4       1 2 3               4 3 2 1     1 2 3
1 2 3 4 5     1 2               5 4 3 2 1     1 2
1 2 3 4 5 6   1               6 5 4 3 2 1     1
"""

# Pattern A
print("Pattern A")
for i in range(1, 7):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Pattern B
print("Pattern B")
for i in range(1, 7):
    for j in range(1, 8 - i):
        print(j, end=" ")
    print()

# Pattern C
print("Pattern C")
for i in range(1, 7):
    for j in range(1, 7):
        if j <= 6 - i:
            print(" ", end=" ")
        else:
            print(7 - j, end=" ")
    print()

# Pattern D
print("Pattern D")
for i in range(1, 7):
    for j in range(1, 7):
        if j <= i - 1:
            print(format(" "), end=" ")
        else:
            print(format(j), end=" ")
    print()

