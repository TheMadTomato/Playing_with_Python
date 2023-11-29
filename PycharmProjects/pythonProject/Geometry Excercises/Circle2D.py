"""
(Geometry: The Circle2D class) Define the Circle2D class that contains:
■ Two private float data fields named x and y that specify the center of the circle
with get/set methods.
■ A private data field radius with get/set methods.
■ A constructor that creates a circle with the specified x, y, and radius. The
default values are all 0.
■ A method getArea() that returns the area of the circle.
■ A method getPerimeter() that returns the perimeter of the circle.
■ A method containsPoint(x, y) that returns True if the specified point (x,
y) is inside this circle (see Figure 8.10a).
■ A method contains(circle2D) that returns True if the specified circle is
inside this circle (see Figure 8.10b).
■ A method overlaps(circle2D) that returns True if the specified circle
overlaps with this circle (see Figure 8.10c).
■ Implement the _ _contains_ _(another) method that returns True if this
circle is contained in another circle.
■ Implement the _ _cmp_ _, _ _lt_ _, _ _le_ _, _ _eq_ _, _ _ne_ _, _ _gt_ _,
_ _ge_ _ methods that compare two circles based on their radius.
"""
import math

class Circle2D:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__radius = 0

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getRadius(self):
        return self.__radius

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def setRadius(self, radius):
        self.__radius = radius

    def getArea(self):
        return math.pi * self.__radius ** 2

    def getPerimeter(self):
        return 2 * math.pi * self.__radius

    def containsPoint(self, x, y):
        return math.sqrt((x - self.__x) ** 2 + (y - self.__y) ** 2) < self.__radius

    def contains(self, circle2D):
        return math.sqrt((self.__x - circle2D.getX()) ** 2 + (self.__y - circle2D.getY()) ** 2) + circle2D.getRadius() < self.__radius

    def overlaps(self, circle2D):
        return math.sqrt((self.__x - circle2D.getX()) ** 2 + (self.__y - circle2D.getY()) ** 2) < self.__radius + circle2D.getRadius()

    def __contains__(self, another):
        return math.sqrt((self.__x - another.getX()) ** 2 + (self.__y - another.getY()) ** 2) + another.getRadius() < self.__radius

    def __cmp__(self, another):
        if self.__radius > another.getRadius():
            return 1
        elif self.__radius < another.getRadius():
            return -1
        else:
            return 0

    def __lt__(self, another):
        return self.__radius < another.getRadius()

    def __le__(self, another):
        return self.__radius <= another.getRadius()

    def __eq__(self, another):
        return self.__radius == another.getRadius()

    def __ne__(self, another):
        return self.__radius != another.getRadius()

    def __gt__(self, another):
        return self.__radius > another.getRadius()

    def __ge__(self, another):
        return self.__radius >= another.getRadius()

# test
c1 = Circle2D()
c2 = Circle2D()
c1.setRadius(5)
c2.setRadius(3)
print(c1.contains(c2))
print(c1.overlaps(c2))
print(c1.__contains__(c2))
print(c1.__cmp__(c2))
print(c1.__lt__(c2))
print(c1.__le__(c2))
print(c1.__eq__(c2))
print(c1.__ne__(c2))
print(c1.__gt__(c2))
print(c1.__ge__(c2))
