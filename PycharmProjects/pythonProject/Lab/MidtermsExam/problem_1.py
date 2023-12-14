"""
Car Plate Numbers Generator.
In Lebanon, people nowadays are buying a special plate numbers 3 digits, 4 digits and 5 digits.
Assume you are working in the Lebanese’s Vehicles Registration as Developer, and you were
asked to develop a Python program to let the buyer print the available car plate numbers based on
the below conditions.
• Buyer will be asked if he/she wants to print/ buy the 3, 4 or 5 digits. (5 points)
• If he/she select 4, then he/she should specify the start digit and the last digit (5 points)
• If he/she select 3 digits, then he/she should specify only the first digit. (5 points)
• If he/she selects 5 digits, he/she should specify the first digit and the third digit. (5 points)
• If he/she enter different than number (3,4 or 5) the program will ask to enter the value
again. (5 points)
After the input the system should print the first 5 numbers. (15 points)
Example: The Buyer select 5 digits and the first and third digit is 3. So, it should print
3231, 3331, 3332, 3431, 3432 and so on.
"""
def generate_numbers(num_digits, first_digit, third_digit=None, last_digit=None):
    # initialize list of numbers
    numbers = []
    # we raise 10 to the power of num_digits - 1 to get the start number and 10 to the power of num_digits to get the end number
    # for example, if num_digits is 3, then start = 10**(3-1) = 10**2 = 100 and end = 10**3 = 1000
    start = 10**(num_digits-1)
    end = 10**num_digits
    # loop through the range of numbers and check if the first digit is equal to the first_digit argument
    for num in range(start, end):
        # convert the number to string to be able to access the digits
        str_num = str(num)
        # check if the first digit is equal to the first_digit argument and the third digit is equal to the third_digit argument and the last digit is equal to the last_digit argument
        # if the third_digit or last_digit is None, then we don't check for it
        # by using none, we can use the same function for 3, 4, and 5 digits
        if str_num[0] == str(first_digit) and (third_digit is None or str_num[2] == str(third_digit)) and (last_digit is None or str_num[-1] == str(last_digit)):
            numbers.append(num)
            if len(numbers) == 5:
                break
    return numbers

while True:
    num_digits = input("Enter the number of digits you want (3, 4, or 5): ")
    if num_digits in ['3', '4', '5']:
        num_digits = int(num_digits)
        first_digit = input("Enter the first digit: ")
        if num_digits == 3:
            numbers = generate_numbers(num_digits, first_digit)
        elif num_digits == 4:
            last_digit = input("Enter the last digit: ")
            numbers = generate_numbers(num_digits, first_digit, last_digit=last_digit)
        elif num_digits == 5:
            third_digit = input("Enter the third digit: ")
            numbers = generate_numbers(num_digits, first_digit, third_digit=third_digit)
        print("The first 5 numbers are: ", numbers)
        break
    else:
        print("Invalid input. Please enter 3, 4, or 5.")
