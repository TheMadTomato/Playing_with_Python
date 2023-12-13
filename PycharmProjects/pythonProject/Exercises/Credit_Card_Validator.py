"""
You need to verify if the given credit card number is valid. For that you need to use the Luhn test.

Here is the Luhn formula:
1. Reverse the number.
2. Multiple every second digit by 2.
3. Subtract 9 from all numbers higher than 9.
4. Add all the digits together.
5. Modulo 10 of that sum should be equal to 0.

Task:
Given a credit card number, validate that it is valid using the Luhn test. Also, all valid cards must have exactly 16 digits.

Input Format:
A string containing the credit card number you need to verify.

Output Format:
A string: 'valid' in case the input is a valid credit card number (passes the Luhn test and is 16 digits long), or 'not valid', if it's not.

Sample Input:
4091131560563988

Sample Output:
valid
"""
def luhn_formula(card_number):
    card_number = card_number[::-1]
    for i in range(1, len(card_number), 2):
        temp = int(card_number[i]) * 2
        if temp > 9:
            temp -= 9
        card_number = card_number[:i] + str(temp) + card_number[i+1:]
    return card_number

while True:
    try:
        card_number = input("Enter credit card number: ")
        if len(card_number) == 16:
            break
    except ValueError:
        print("Please enter a valid credit card number")

card_number = luhn_formula(card_number)
total = 0
for i in card_number:
    total += int(i)

if total % 10 == 0:
    print("valid")
else:
    print("not valid")