"""
Credit cards numbers follow certain patterns: It must have between 13 nad 16 digits, and the number must start with:
4 for Visa cards
5 for Master cards
37 for American Express cards
6 for Discover cards

in 1954, Hans Luhn of IBM proposed an algorithm for validating credit card numbers. The algorithm is useful to determine
whether a card number is entered correctly or whether a credit card is scanned correctly by a scanner. Credit card
numbers are generated following this validity check, commonly known a the Luhn check or the Mod 10 check, which can be
described as follows (for illustration, consider the card number 4388576018402626):
1. Double every second digit from right to left. If doubling of a digit results in a two-digit number, add up the two
   digits to get a single-digit number.
2. Now add all single-digit numbers from Step 1.
    4 + 4 + 8 + 2 + 3 + 1 + 7 + 8 = 37
3. Add all digits in the odd places from right to left in the card number.
    6 + 6 + 0 + 8 + 0 + 7 + 8 + 3 = 38
4. Sum the results from Step 2 and Step 3.
    37 + 38 = 75
5. If the result from Step 4 is divisible by 10, the card number is valid; otherwise, it is invalid. For example, the
    number 4388576018402626 is invalid, but the number 4388576018410707 is valid.

Write a program that prompts the user to enter a credit card number as a long integer. Display whether the number is
valid or invalid. Design your program to use the following functions:
# Return true if the card number is valid
def isValid(number):
# Get the result from Step 2
def sumOfDoubleEvenPlace(number):
# Return this number if it is a single digit, otherwise, return the sum of the two digits
def getDigit(number):
# Return sum of odd-place digits in number
def sumOfOddPlace(number):
# Return true if the digit d is a prefix for number
def prefixMatched(number, d):
# Return the number of digits in d
def getSize(d):
# Return the first k number of digits from number. If the number of digits in number is less than k, return number.
def getPrefix(number, k):

"""
# Return true if the card number is valid
def isValid(number: int) -> bool:
    sum = sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)
    return sum % 10 == 0 and prefixMatched(number, 4) or prefixMatched(number, 5) or prefixMatched(number, 37) \
        or prefixMatched(number, 6) and getSize(number) >= 13 and getSize(number) <= 16

# Get the result from Step 2
def sumOfDoubleEvenPlace(number: int) -> int:
    sum = 0
    for i in range(len(str(number)) - 2, -1, -2): #
        sum += getDigit(int(str(number)[i]) * 2)
    return sum

# Return this number if it is a single digit, otherwise, return the sum of the two digits
def getDigit(number: int) -> int:
   if number < 10:
       return number
   else:
       return number % 10 + number // 10

# Return sum of odd-place digits in number
def sumOfOddPlace(number: int) -> int:
    sum = 0
    for i in range (len(str(number)) - 1, -1, -2):
        sum += int(str(number)[i])
    return sum

# Return true if the digit d is a prefix for number
def prefixMatched(number: int, d: int) -> bool:
    return getPrefix(number, getSize(d)) == d

# Return the number of digits in d
def getSize(d: int) -> int:
    return len(str(d))

# Return the first k number of digits from number. If the number of digits in number is less than k, return number.
def getPrefix(number: int, k: int) -> int:
    return int(str(number)[:k])

def main():
    number = eval(input("Enter a credit card number as a long integer: "))
    if isValid(number):
        print(f"{number} is valid")
    else:
        print(f"{number} is invalid")

main()