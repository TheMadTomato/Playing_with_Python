"""
 (Compute pi ) You can approximate pi by using the following series:

 pi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ... + (-1)^(i+1)/(2i-1))

 Write a program that displays the pi value for i = 10000, 20000, . . ., and
"""
for i in range(10000, 100001, 10000):
    sum = 0
    for j in range(1, i + 1):
        sum += ((-1) ** (j + 1)) / (2 * j - 1)

    pi = 4 * sum
    print("PI value for i=", i, "is", pi)