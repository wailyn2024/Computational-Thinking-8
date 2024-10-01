#setup
import turtle
import random
colors = ["red", "orange","yellow", "green", "blue", "indigo", "violet"]
numberlist = [1,2,3,4,5]
t = turtle.Turtle()
t2 = turtle.Turtle()
r = random.Random()
t.goto(0,0)
t.color("green")
t.speed(100)
t.pendown()
color = r.choice(colors)
t.fillcolor(color)
t.begin_fill()
angle = (1)
forward = (10)
#t2 setup
t2.goto(0,0)
t2.color("green")
t2.speed(100)
t2.pendown()
t2.left(180)
forward2 = (10)
t2.fillcolor(color)
t2.begin_fill()
#turtle one
for i in range(1000):
    t.forward(forward)
    t.left(angle)
    color = r.choice(colors)
    t.color(color)
    angle = angle + r.choice(numberlist)
    coords = t.pos()
    x,y = coords
    if x > 350 or x < -350 or y > 300 or y < -300:
        t.penup()
        t.goto(0,0)
        t.pendown()
    #turtle two
    t2.forward(forward)
    t2.left(angle)
    t2.color(color)
    coords2 = t2.pos()
    x2,y2 = coords2
    if x2 > 350 or x2 < -350 or y2 > 300 or y2 < -300:
        t2.penup()
        t2.goto(0,0)
        t2.pendown()
t.end_fill()
t2.end_fill()
#end
turtle.exitonclick()