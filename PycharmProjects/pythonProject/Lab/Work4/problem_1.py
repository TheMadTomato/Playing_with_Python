"""
Write a Python script that will prompt the user to enter two numbers where:
• Number 1 (n1) is less than Number 2 (n2)
• Both numbers are between 1024 and 5120 (inclusive)
Then the script must output the numbers that have all digits even and are between n1 and n2. 
"""

# take input 1 and 2 with the condition that n1 is less than n2 and the 2 nuber between 1024 and 5120 with try excpet block:

while True:
    try:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        if number1 < number2 and 1024 <= number1 <= 5120 and 1024 <= number2 <= 5120:
            break
        else:
            print("Please enter the number again")
    except ValueError:
        print("Please enter the number again")

# initializing list
num_list = list()

# Display first message
print(f"The numbers between {number1} and {number2} that have all digits even, are: ")

# Generating the list content with for loop
for i in range(number1, number2+1):
    if i % 2 == 0:
        num_list.append(i)
        temp = i # temp variable so we can check each digit in it if it is even or odd
        # Checking each digit in the number if it is even or odd by dividing it by 10 then check the remainder
        while temp > 0:
            if temp % 2 == 0:
                temp = temp // 10
            else:
                # if the digit is odd then remove the number from the list and break the loop
                num_list.pop()
                break
    else:
        continue

# Display list
print(num_list)
