import turtle
import random

turtle.speed(1) # slowest speed

# draw 16 by 16 lattice
turtle.color("gray") # color of the lattice
x = -80
for y in range(-80, 80 + 1, 10):
    turtle.penup()
    turtle.goto(x, y) # draw horizontal lines
    turtle.pendown()
    turtle.forward(160)

y = 80
turtle.right(90)
for x in range(-80, 80 + 1, 10):
    turtle.penup()
    turtle.goto(x, y) # draw vertical lines
    turtle.pendown()
    turtle.forward(160)

turtle.pensize(3)
turtle.color("red")

# draw a random walk
turtle.penup()
turtle.goto(0, 0) # start from the center
turtle.pendown()

x = y = 0 # current pen location at the center
while abs(x) < 80 and abs(y) < 80:
    r = random.randint(0, 3)
    if r == 0:
        x += 10 # move right
        turtle.setheading(0)
        turtle.forward(10)
    elif r == 1:
        y -= 10 # move down
        turtle.setheading(270)
        turtle.forward(10)
    elif r == 2:
        x -= 10 # move left
        turtle.setheading(180)
        turtle.forward(10)
    elif r == 3:
        y += 10 # move up
        turtle.setheading(90)
        turtle.forward(10)

turtle.done()
