import math as m
import sympy as s

def isPrime(n):
    # Returns True if n is prime, False otherwise
    if n <= 1:
        return False
    for i in range(2, m.ceil(m.sqrt(n))):
        if n % i == 0:
            return False
    return True

def isEven(n):
    # Returns True if n is even, False otherwise
    return n % 2 == 0

def isOdd(n):
    # Returns True if n is odd, False otherwise
    return not isEven(n)

def isPerfect(n):
    # Returns True if n is perfect, False otherwise
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

def isPerfectSquare(n):
    # Returns True if n is a perfect square, False otherwise
    return m.sqrt(n) % 1 == 0

def GCD(a, b):
    # Returns the Greatest Ccommon Diviser of a and b
    if b == 0:
        return a
    return GCD(b, a % b)

def LCM(a, b):
    # Returns the Lowest Common Multiplier of a and b
    return a * b // GCD(a, b)

def factorial(n):
    # Returns the factorial of n
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    # Returns the n-th Fibonacci number
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def isFibonacci(n):
    # Returns True if n is a Fibonacci number, False otherwise
    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)

def divSum(n):
    # Returns the sum of the divisors of n
    sum: int = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

def isFreind(a,b):
    return divSum(a) == b and divSum(b) == a and a != b and b != a

