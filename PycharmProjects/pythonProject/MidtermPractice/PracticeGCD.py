# find the greatest common divisor of two numbers

print("##Method 1##")
n1, n2 = eval(input("Enter n1, n2: "))
gcd = 1
k = 2
while k <= n1 and k <= n2:
    if n1 % k == 0 and n2 % k == 0:
        gcd = k
    k += 1

print("The greatest common divisor for", n1, "and", n2, "is", gcd)

########################################################################
print("##Method 2##")
m1, m2 = eval(input("Enter m1, m2: "))
mgcd =0

if m1 < m2:
    smaller = m1
else:
    smaller = m2
for i in range(1, smaller+1):
    if((m1 % i == 0) and (m2 % i == 0)):
        mgcd = i
print("gcd in method#2 is", mgcd)