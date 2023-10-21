"""
Try-Catch:
Write a python program to let the user to enter integer number only if not
he/she will try again
"""

# Main Loop
while True:
    try:
        usr_input = int(input("Enter an integer: "))
        print(f"Your input {usr_input} is an integer")
        break
    except:
        print("Invalid input. Try again.")