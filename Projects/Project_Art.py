#set up
import turtle, random
#variables
colors = ["orchid","teal","cyan"]
colors2 = ["indianred","salmon", "coral", "lightcoral"]
background = ["gold", "magenta"]
#turtle start
t = turtle.Turtle()
t.penup()
t.goto(0,0)
t.pendown()
#the object
for i in range(500):
    turtle.bgcolor(random.choice(background))
    t.color(random.choice(colors))
    t.speed(100)
    t.forward(50+i)
    t.left(120+1)
t.penup()
t.goto( 0, 0)
t.pendown()
for i in range(400):
    turtle.bgcolor(random.choice(background))
    t.forward(50+i)
    t.left(144+1)
    t.color(random.choice(colors2))
turtle.bgcolor("navy")
turtle.exitonclick()
