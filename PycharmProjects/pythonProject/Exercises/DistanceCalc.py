import math


def distanceCalc(x1, y1, x2, y2):
    # The Formuala is √[(x2 − x1)2 + (y2 − y1)2]
    Distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    return Distance


# Take Input
x1, y1 = eval(input("Enter coordinates x1, x2: "))
x2, y2 = eval(input("Enter coordinates y1, y2: "))

# Print result
distance = distanceCalc(x1, y1, x2, y2)
print("The distance between is: %.2f" % distance)
