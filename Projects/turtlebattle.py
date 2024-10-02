# ###############################################
# ### SETUP ###
import turtle
import time
import random
# ############################################### vars
game = True
a = turtle.Turtle()
a.penup()
a.goto(-100, -100)
a.color("red")
a.pendown()

b = turtle.Turtle()
b.penup()
b.goto(-100, -100)
b.color("blue")
b.pendown()

c = turtle.Turtle()
c.penup()
c.goto(-100, -100)
c.color("green")
c.pendown()

d = turtle.Turtle()
d.penup()
d.goto(-100, -100)
d.color("yellow")
d.pendown()

while game:
    a.forward(1)
    a.left(random.randint(-15,15))
    b.forward(1)
    b.left(random.randint(-15,15))
    c.forward(1)
    c.left(random.randint(-15,15))
    d.forward(1)
    d.left(random.randint(-15,15))