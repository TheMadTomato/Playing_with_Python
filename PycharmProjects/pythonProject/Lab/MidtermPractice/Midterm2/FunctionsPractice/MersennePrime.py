"""
(Mersenne prime) A prime number is called a Mersenne prime if it can be written
in the form 2p - 1 for some positive integer p. Write a program that finds all
Mersenne primes with p ... 31 and displays the output as follows:
        p       2^p - 1
        2       3
        3       7
        5       31
"""
def isPrime(num: int) -> bool:
    divisor = 2
    while divisor <= num / 2:
        if num % divisor == 0:
            return False
        divisor += 1
    return True

def isMersennPrime(num: int) -> bool:
    return isPrime(2 ** num - 1)

def main():
    print("P\t2^P-1")
    for i in range(2, 32):
        if isMersennPrime(i):
            print(i, "\t", 2 ** i - 1)

main()

"""
Output:
P	2^P-1
2 	 3
3 	 7
5 	 31
7 	 127
13 	 8191
17 	 131071
19 	 524287
31 	 2147483647
"""