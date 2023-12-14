"""
(Display numbers in a pyramid pattern) Write a nested for loop that displays the
following output:
                            1
                        1   2   1
                    1   2   4   2   1
                1   2   4   8   4   2   1
            1   2   4   8   16  8   4   2   1
        1   2   4   8   16  32  16  8   4   2   1
    1   2   4   8   16  32  64  32  16  8   4   2   1
"""
for i in range(1, 8):
    for j in range(1, 8 - i):
        print(format(" ", "4s"), end="")
    for y in range(1, i + 1):
        print(format(2 ** (y - 1), "4d"), end="")
    for z in range(i - 1, 0, -1):
        print(format(2 ** (z - 1), "4d"), end="")
    print()