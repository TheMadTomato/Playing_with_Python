# Lottery
import random

# Generate a random number
random_num = str(random.randint(100000, 999999))


# User Guess
user_guess = input("Enter a 6 digit number: ")

# Check if user guess is correct and output what prize he get
## if the user guess match the lottery in the exact order, the award is 10,000
if user_guess == random_num:
    print("You won $10,000")

## if all the digits in the user guess match all the digits in the lottery, the award is 3,000
elif user_guess in random_num:
    print("You won $3,000")

## if one digit in the user guess match a digit in the lottery, the award is 1,000
elif user_guess[0] in random_num or user_guess[1] in random_num or user_guess[2] in random_num or user_guess[3] in random_num or user_guess[4] in random_num or user_guess[5] in random_num:
    print("You won $1,000")

else:
    print("Sorry, no match")

# Output the lottery number
print("The lottery number is: ", random_num)
