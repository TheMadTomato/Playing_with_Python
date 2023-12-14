"""
 (Sum a series) Write a program to sum the following series:
    1/3 + 3/5 + 5/7 + 7/9 + 9/11 + ... + 95/97 + 97/99

"""
sum = 0
for i in range(1, 99, 2):
    # this sequence is a series of consecutive odd numbers in numerator and denominator
    # we can use i to represent the numerator and i + 2 to represent the denominator
        sum += i/(i+2)

print(f"Sum = {sum}")

