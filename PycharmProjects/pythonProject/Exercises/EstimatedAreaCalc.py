import math


def distanceCalc(x1, y1, x2, y2):
    # The Formuala is √[(x2 − x1)2 + (y2 − y1)2]
    Distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    return Distance
def triangleAreaCalc(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    triangle_area = math.sqrt(s * (s - side1)*(s - side2)*(s - side3))
    return triangle_area


print("**Estimated 4 points Area Calculator**")

# Taking Coordinates of 8 areas
x1, y1 = eval(input("Enter the Coordinate of Area 1: "))
x2, y2 = eval(input("Enter the Coordinate of Area 2: "))
x3, y3 = eval(input("Enter the Coordinate of Area 3: "))
x4, y4 = eval(input("Enter the Coordinate of Area 4: "))

# Calculating the distances between each point
distance_1_to_2 = distanceCalc(x1, y1, x2, y2)
distance_2_to_3 = distanceCalc(x2, y2, x3, y3)
distance_3_to_4 = distanceCalc(x3, y3, x4, y4)
distance_4_to_1 = distanceCalc(x4, y4, x1, y1)

# 4 points mean 4 corner meaning to calculate the area inside these 4 point.
# we compute the area of the 2 triangle inside the area

distance_2_to_4 = distanceCalc(x2, y2, x4, y4) # to calculate the area of a triangle

estimated_area_half_1 = triangleAreaCalc(distance_1_to_2, distance_2_to_4, distance_4_to_1)
estimated_area_half_2 = triangleAreaCalc(distance_2_to_3, distance_3_to_4, distance_2_to_4)

# Final result
estimated_area = estimated_area_half_1 + estimated_area_half_2

print("The estimated area inside these 4 Coordinates is %.3f" % estimated_area)