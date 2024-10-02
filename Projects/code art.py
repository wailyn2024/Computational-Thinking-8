

import turtle, random, math
turtle.goto(-100,100)
t = turtle.Turtle()
#turle colors
turtle.bgcolor("LightCyan")
#turle size
t.speed(20)
t.shapesize(5)
colors = ["Violet","MediumSpringGreen","Pink"]
angles = [5, 5, 6]
sides = [7]
for i in range(100000):
#turtle drawing color
    t.color(random.choice(colors))
    t.forward(random.choice(sides))
    t.left(121)
    t.back(300)
    # if abs(t.xcor()) > or abs(t.ycor()):
    #     t.penup()
    #     t.goto(0,0)
    #     t.pendown()


turtle.exitonclick()       







