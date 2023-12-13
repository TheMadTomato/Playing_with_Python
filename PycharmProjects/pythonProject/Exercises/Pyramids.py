"""
(Display a pyramid ) Write a program that prompts the user to enter an integer
from 1 to 15 and displays a pyramid, as shown in the following sample run:
"""
# Get input from user
number = eval(input("Enter the number of lines: "))

# Display pyramid
for i in range(1, number + 1):
    # Display spaces
    for j in range(number - i, 0, -1):
        print(" ", end=" ")
    # Display left half of pyramid
    for k in range(i, 0, -1):
        print(k, end=" ")
    # Display right half of pyramid
    for l in range(2, i + 1):
        print(l, end=" ")
    print()