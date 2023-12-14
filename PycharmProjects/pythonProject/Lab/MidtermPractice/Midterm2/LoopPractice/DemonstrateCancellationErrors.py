"""
(Demonstrate cancellation errors) A cancellation error occurs when you are
manipulating a very large number with a very small number. The large number
may cancel out the smaller number. For example, the result of 100000000.0 +
0.000000001 is equal to 100000000.0. To avoid cancellation errors and obtain
more accurate results, carefully select the order of computation. For example, in
computing the following series, you will obtain more accurate results by comput-
ing from right to left rather than from left to right:
1 + 1/2 + 1/3 + ... + 1/n
Write a program that compares the results of the summation of the preceding
series, computing both from left to right and from right to left with n = 50000.
"""
# left to right
left_to_right = 0
for i in range(1, 50000 + 1):
    left_to_right += 1 / i
print(f"left to right: {left_to_right}")

# right to left
right_to_left = 0
for i in range(50000, 0, -1):
    right_to_left += 1 / i
print(f"right to left: {right_to_left}")



