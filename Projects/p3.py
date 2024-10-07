#set up
import turtle
#turtle1
t = turtle.Turtle()
t.speed(100) 
t.penup
t.goto(0,0)
t.pendown
t.color("cyan")
for i in range(150):
    t.forward(100 + i)
    t.left(120)
#turtle2
t2 = turtle.Turtle()
t2.goto (0,100)
t2.color("red")
t2.speed(100)
for i in range(100):
    t2.forward (100 + 10)
    t2.left(90 +1)
    #turtle 
t3 = turtle.Turtle()
t3.goto(0,-100)
t3.speed(100)
t3.color("red")
for i in range (100):
    t3.color("red")
    t3.forward (100 + 10)
    t3.left(90+ 1)

turtle.exitonclick()