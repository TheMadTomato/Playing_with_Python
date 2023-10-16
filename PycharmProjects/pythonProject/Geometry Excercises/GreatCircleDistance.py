import math

# take input
print("Enter point 1 (latitude and longitude) in degrees: ")
x1, y1 = eval(input())
print("Enter point 2 (latitude and longitude) in degrees: ")
x2, y2 = eval(input())

# Convert to Radians
X1 = math.radians(x1)
Y1 = math.radians(y1)
X2 = math.radians(x2)
Y2 = math.radians(y2)

distance = (6371.01 * math.acos(math.sin(X1)) * math.sin(X2)) + (math.cos(X1) * math.cos(X2) * math.cos(Y1 - Y2))
print("The distance between the two point is %13f" % distance)



