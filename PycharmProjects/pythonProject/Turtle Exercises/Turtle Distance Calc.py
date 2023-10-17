import turtle
import math

# Take Input
x1, y1 = eval(input("Enter coordinates x1, y2: "))
x2, y2 = eval(input("Enter coordinates x2, y2: "))

# Print result
distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

# Draw the line with points A and B
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.dot(5)  # Draw a small dot at A
turtle.write("A(%d, %d)" % (x1, y1))

turtle.goto(x2, y2)
turtle.dot(5)  # Draw a small dot at B
turtle.write("B(%d, %d)" % (x2, y2))

# Print the distance
turtle.penup()
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
turtle.write("D = %.2f" % distance)

turtle.done()
