"""
(Display a pyramid ) Write a program that prompts the user to enter an integer
from 1 to 15 and displays a pyramid, as shown in the following sample run:
Enter the number of lines: 7
                  1
                2 1 2
              3 2 1 2 3
            4 3 2 1 2 3 4
          5 4 3 2 1 2 3 4 5
        6 5 4 3 2 1 2 3 4 5 6
      7 6 5 4 3 2 1 2 3 4 5 6 7
"""
num = eval(input("Enter the number of lines: "))
for i in range(1, num + 1):
    # print("i is", i)
    for j in range(1, num + 1):
        # print("j is", j)
        if j <= num - i:
            print(format(" ", "4s"), end="")
        else:
            print(format(j, "4d"), end="")
    for y in range(num - 1, 0, -1):
        if y >= num - i + 1:
            print(format(y, "4d"), end="")
        else:
            print(format(" ", "4s"), end="")
    print()