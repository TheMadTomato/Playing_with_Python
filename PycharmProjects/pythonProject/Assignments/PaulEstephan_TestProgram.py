"""
Test the Class LinearEquation written in the code file PaulEstephan_LinearEquation.py
"""
from PaulEstephan_LinearEquation import LinearEquation

# Test the Class LinearEquation
# Create an object of the class LinearEquation
linearEquation = LinearEquation(1, 2, 3, 4, 5, 6)

# Test the getter methods
print("A is equal to:", linearEquation.get_a())
print("B is equal to:", linearEquation.get_b())
print("C is equal to:", linearEquation.get_c())
print("D is equal to:", linearEquation.get_d())
print("E is equal to:", linearEquation.get_e())
print("F is equal to:", linearEquation.get_f())
print()

# Test the isSolvable() method
print("Is a*d –b*c solvable?", linearEquation.isSolvable())
print()

# Test the getX() and getY() methods
print("X = (e*d – b*f)/(a*d – b*c)")
print(f"X = ({linearEquation.get_e()}*{linearEquation.get_d()} – {linearEquation.get_b()}*{linearEquation.get_f()})/({linearEquation.get_a()}*{linearEquation.get_d()} – {linearEquation.get_b()}*{linearEquation.get_c()})")
print("X = ", linearEquation.getX())
print()
print("Y = (a*f – e*c)/(a*d – b*c)")
print(f"Y = ({linearEquation.get_a()}*{linearEquation.get_f()} – {linearEquation.get_e()}*{linearEquation.get_c()})/({linearEquation.get_a()}*{linearEquation.get_d()} – {linearEquation.get_b()}*{linearEquation.get_c()})")
print(linearEquation.getY())
