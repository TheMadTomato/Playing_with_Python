import math

## Area Functions
def triangleArea(base, height):
    area = (base * height)/2
    return area
def pentagonArea(length):
    side = 2 * length * math.sin(math.pi / 5)
    area = ((3 * math.sqrt(3))/2) * math.pow(side, 2)
    return area

def polygonArea(number_of_sides, side_length):
    polygon_area = (number_of_sides * pow(side_length, 2))/(4 * tan(pi/number_of_sides))
    return polygon_area
def circleArea(radius):
    area = math.pi * math.pow(radius, 2)
    return area
def rectangleArea(length, width):
    area = length * width
    return area
def squareArea(side):
    area = math.pow(side, 2)
    return area
def cylinderArea(radius, height):
    area = 2 * math.pi * radius * height + 2 * math.pi * math.pow(radius, 2)
    return area
def coneArea(radius, height):
    area = math.pi * radius * (radius + math.sqrt(math.pow(height, 2) + math.pow(radius, 2)))
    return area
def sphereArea(radius):
    area = 4 * math.pi * math.pow(radius, 2)
    return area
def cubeArea(side):
    area = 6 * math.pow(side, 2)
    return area
def prismArea(side, height):
    area = 2 * math.pow(side, 2) + 5 * side * height
    return area
def pyramidArea(base, height):
    area = math.pow(base, 2) + 2 * base * height
    return area
def torusArea(r1, r2):
    area = 4 * math.pi * math.pow(r1, 2) * math.pow(r2, 2)
    return area
def trapezoidArea(base1, base2, height):
    area = ((base1 + base2)/2) * height
    return area
def ellipseArea(a, b):
    area = math.pi * a * b
    return area

## Volume Functions
def cubeVolume(side):
    volume = math.pow(side, 3)
    return volume
def sphereVolume(radius):
    volume = (4/3) * math.pi * math.pow(radius, 3)
    return volume
def cylinderVolume(radius, height):
    volume = math.pi * math.pow(radius, 2) * height
    return volume
def coneVolume(radius, height):
    volume = (1/3) * math.pi * math.pow(radius, 2) * height
    return volume
def pyramidVolume(base, height):
    volume = (1/3) * math.pow(base, 2) * height
    return volume
def prismVolume(base, height):
    volume = base * height
    return volume
def torusVolume(r1, r2):
    volume = 2 * math.pi * math.pow(r2, 2) * math.pow(r1, 2)
    return volume
def ellipsoidVolume(a, b, c):
    volume = (4/3) * math.pi * a * b * c
    return volume

## Basic Geometry Functions
def pythagoras(a, b):
    c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
    return c
def distance(x1, y1, x2, y2):
    distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    return distance
def midpoint(x1, y1, x2, y2):
    midpoint = ((x1 + x2)/2, (y1 + y2)/2)
    return midpoint
def slope(x1, y1, x2, y2):
    slope = (y2 - y1)/(x2 - x1)
    return slope

