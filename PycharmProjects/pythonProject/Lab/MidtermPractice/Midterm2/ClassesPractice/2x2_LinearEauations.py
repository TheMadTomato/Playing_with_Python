"""
Design a class named LinearEquation for a
2 * 2 system of linear equations:

ax + by = e     x = (ed - bf) / (ad - bc)
cx + dy = f     y = (af - ec) / (ad - bc)

The class contains:
■ The private data fields a, b, c, d, e, and f with get methods.
■ A constructor with the arguments for a, b, c, d, e, and f.
■ Six get methods for a, b, c, d, e, and f.
■ A method named isSolvable() that returns true if ad - bc is not 0.
■ The methods getX() and getY() that return the solution for the equation.
Draw the UML diagram for the class, and then implement the class. Write a test
program that prompts the user to enter a, b, c, d, e, and f and displays the result.
If ad - bc is 0, report that “The equation has no solution.” 
"""

class LineaerEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    # getters
    def getA(self):
        return self.__a
    def getB(self):
        return self.__b
    def getC(self):
        return self.__c
    def getD(self):
        return self.__d
    def getE(self):
        return self.__e
    def getF(self):
        return self.__f

    # methods

    def isSolvable(self):
        return self.__a * self.__d - self.__b * self.__c != 0

    def getX(self):
        return (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)

    def getY(self):
        return (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)


# test
eq = LineaerEquation(1, 2, 3, 4, 5, 6)
print(eq.isSolvable())
print(eq.getX())
print(eq.getY())