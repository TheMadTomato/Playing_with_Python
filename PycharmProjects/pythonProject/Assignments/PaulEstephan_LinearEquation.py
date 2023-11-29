"""
Design a class named LinearEquation for a 2*2 system of linear equations:

        a*x + b*y = e       x = (e*d – b*f)/(a*d – b*c)     y = (a*f – e*c)/(a*d – b*c)     c*x + d*y = f

The class contains:
    ■ Private data fields a, b, c, d, e, and f.
    ■ A constructor with the arguments for a, b, c, d, e, and f.
    ■ Six getter methods for a, b, c, d, e, and f.
    ■ A method named isSolvable() that returns true if ad – bc is not 0.
    ■ Methods getX() and getY() that return the solution for the equation.
N.B: 1- If a*d –b*c is 0, report that “The equation has no solution.
"""

class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        # Private data fields a, b, c, d, e, and f.
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
        self.__d = float(d)
        self.__e = float(e)
        self.__f = float(f)

    # Six getter methods for a, b, c, d, e, and f.
    ## getter are used to access the private data fields
    def get_a(self):
        return self.__a
    def get_b(self):
        return self.__b
    def get_c(self):
        return self.__c
    def get_d(self):
        return self.__d
    def get_e(self):
        return self.__e
    def get_f(self):
        return self.__f

    # A method named isSolvable() that returns true if ad – bc is not 0.
    # and a string "The equation has no solution" if ad – bc is 0.
    def isSolvable(self):
        if (self.__a * self.__d) - (self.__b * self.__c) != 0:
            return True
        else:
            return "The equation has no solution"

    # Methods getX() and getY() that return the solution for the equation.
    # if isSolvable() returns False, then getX() and getY() return False
    def getX(self):
        if self.isSolvable():
            return (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)
        else:
            return False

    def getY(self):
        if self.isSolvable():
            return (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)
        else:
            return False