"""
A Monte Carlo simulation uses random numbers and probability to solve problems. It has a
wide range of applications in computational mathematics, physics, chemistry, and finance.
We now look at an example of using a Monte Carlo simulation for estimating pi.
First, draw a circle with its bounding square.

Assume the radius of the circle is 1. So, the circle area is p and the square area is 4. Ran-
domly generate a point in the square. The probability that the point falls in the circle is
circleArea / squareArea = π / 4.
Write a program that randomly generates 1000000 points that fall in the square and let
numberOfHits denote the number of points that fall in the circle. So, numberOfHits is
approximately 1000000 * (π / 4). p can be approximated as 4 * numberOfHits /
1000000.
"""
import random

NumberOfTrials = 1000000
NumberOfHits = 0

for i in range(NumberOfTrials):
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1
    if x * x + y * y <= 1:
        NumberOfHits += 1

pi = 4 * NumberOfHits / NumberOfTrials
print("pi is", pi)