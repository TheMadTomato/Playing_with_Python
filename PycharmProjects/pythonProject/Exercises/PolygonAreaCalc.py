from math import pow, tan, pi

number_of_sides = eval(input("Enter the number of sides: "))
side_length = eval(input("Enter Side length: "))

polygon_area = (number_of_sides * pow(side_length, 2))/(4 * tan(pi/number_of_sides))

print("The area of the polygon is %f" % polygon_area)