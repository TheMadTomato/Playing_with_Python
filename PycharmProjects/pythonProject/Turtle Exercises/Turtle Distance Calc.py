import turtle
import math

# Take Input
x1, y1 = eval(input("Enter coordinates x1, y2: "))
x2, y2 = eval(input("Enter coordinates x2, y2: "))

# Print result
distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

# Draw the line
turtle.penup()
## mark the first point labeled as (x1, y1)
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("%d, %d" % (x1, y1))

## mark the second point labeled as (x2, y2)
turtle.goto(x2, y2)
turtle.write("%d, %d" % (x2, y2))

# Print the distance
turtle.penup()
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
turtle.write(distance)

turtle.done()