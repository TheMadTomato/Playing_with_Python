"""
(Emirp) An emirp ( prime spelled backward) is a nonpalindromic prime number
whose reversal is also a prime. For example, both 17 and 71 are prime numbers, so
17 and 71 are emirps. Write a program that displays the first 100 emirps. Display
10 numbers per line and align the numbers properly, as follows:
13 17 31 37 71 73 79 97 107 113
149 157 167 179 199 311 337 347 359 389
...
"""
# function to check if number is prime
def isPrime(num: int) -> bool:
    divisor = 2
    while divisor <= num / 2:
        if num % divisor == 0:
            return False
        divisor += 1
    return True
def isEmirp(num1, num2) -> bool:
    return isPrime(num1) and isPrime(num2)

def main():
    count = 0
    counter = 0
    for i in range(13, 10000):
        if isEmirp(i, int(str(i)[::-1])):
            count += 1
            print(i, end=" ")
            counter += 1
            if count % 10 == 0:
                print()
            if counter == 100:
                break


main()