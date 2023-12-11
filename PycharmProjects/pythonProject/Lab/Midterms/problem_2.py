"""
Guessing Game:
Write a Python script that generates a random integer from 1 to 100, then asks the player to guess
that number. Game rules:
1. If the player enters a number less than 1 or greater than 100, print "OFF-LIMITS"
2. If the player guessed the number print "SPOT ON!" and exit
3. On the first player guess:
1. If the guess is within 10 of the number, print "CLOSE!"
2. If the guess is further away than that, print "FAR!"
4- At the end of the game, print out the number of guesses
"""
import random

# Generate random number
random_number = random.randint(1, 100)


# Function to check if the number is within 10 of the random number
def is_close(number):
    return random_number - 10 <= number <= random_number + 10


# counter
tries = 0

# Welcome message
print("Welcome to the guessing game!\n"
      "Your job is to guess the number that i generated that is between 1 and 100.\n")
# Main Loop
while True:
    # Get user input
    user_input = int(input("Enter a number: "))
    tries += 1
    # Check if the user input is within the range
    if user_input < 1 or user_input > 100:
        print("OFF-LIMITS")
        break
    # Check if the user input is the random number
    elif user_input == random_number:
        print("SPOT ON!")
        break
    elif tries == 1:
        # Check if the number is within 10 of the random number
        # We check the following code only once to let the closer/farther logic work
        if is_close(user_input):
            print("CLOSE!\n")
        else:
            print("FAR!\n")
    # Check if the number is within 10 of the random number
    elif is_close(user_input) and user_input != random_number:
        print("CLOSER\n")
    elif not is_close(user_input) and user_input != random_number:
        print("FARTHER\n")


# How many tries until "SPOT ON"
print(f"\nIt took you {tries} tries to guess the number")

