#imports
import turtle, random
#turtle
t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("red")
t.pendown()
t.speed(1000)
b = turtle.Turtle()
b.penup()
b.goto(-99, -100)
b.color("red")
b.pendown()
b.speed(1000)
#vars
tcolors = ["red","gray","yellow",]
bcolors = ["blue","green","purple",]
directions = [90,180,270,360]
#running
for i in range (1000):
    t.forward(10)
    t.left(random.choice(directions))
    b.forward(10)
    b.left(random.choice(directions))
    t.color(random.choice(tcolors))
    b.color(random.choice(bcolors))   