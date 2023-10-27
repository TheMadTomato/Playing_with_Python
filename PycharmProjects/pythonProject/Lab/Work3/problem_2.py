"""
Write a python program to develop the below stars, the side of square
should be entered by the user
"""

# Square Length and width input. try length: 5 & width = 9
length = eval(input("Enter length: "))
width = eval(input("Enter width: "))

# Neste for to draw square
for row in range (length):
    for col in range (width):
        # Condition for a hollow swuare
        if row == 0 or row == length - 1 or col == 0 or col == width - 1:
            # The Following if else is to let the square look like the output in the problem
            if col % 2 == 1:
                print(" ", end="")
            else:
                print("*", end="")
        else:
            print(" ", end="")
    print()
