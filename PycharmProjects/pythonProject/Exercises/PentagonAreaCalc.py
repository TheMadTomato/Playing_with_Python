import math

length = eval(input("Enter the length from the center to a vertex: "))

side = 2 * length * math.sin(math.pi / 5)
area = ((3 * math.sqrt(3))/2) * math.pow(side, 2)
print("The area of the pentagon is %.2f" % area)