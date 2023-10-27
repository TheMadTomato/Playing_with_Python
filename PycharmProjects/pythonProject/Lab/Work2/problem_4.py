from math import pi

# function to convert degrees to radians
def degrees_to_radians(degrees):
    return degrees * pi / 180

# take input and convert to radians
angle = eval(input("Inpute in value in degrees: "))
print("%f in degree is %f in radians" % (angle, degrees_to_radians(angle)))