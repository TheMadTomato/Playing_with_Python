#Prompt  the user to enter two integers

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

gcd = 1
k = 2

while k <= num1 and k <= num2:
    if num1 % k == 0 and num2 % k == 0:
        gcd = k
    k += 1

print("The greatest common divisor for", num1, "and", num2, "is", gcd)