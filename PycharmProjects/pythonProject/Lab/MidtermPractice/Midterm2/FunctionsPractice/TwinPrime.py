"""
(Twin primes) Twin primes are a pair of prime numbers that differ by 2. For exam-
ple, 3 and 5, 5 and 7, and 11 and 13 are twin primes. Write a program to find all
twin primes less than 1,000. Display the output as follows:
(3, 5)
(5, 7)...
"""
def isPrime(num: int) -> bool:
    divisor = 2
    while divisor <= num / 2:
        if num % divisor == 0:
            return False
        divisor += 1
    return True
def main():
    print("="*3, "Twin Primes".center(10), "="*3)
    for i in range(2, 1000):
        if isPrime(i) and isPrime(i + 2):
            print(f"({i}, {i + 2})")

main()