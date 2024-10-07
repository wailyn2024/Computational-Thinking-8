import turtle

t = turtle
t.speed(100)
t.goto(-100, -100)
t.color("cyan")
for i in range(100):
    t.forward(100 + i)
    t.left(120 + 1)
t.penup
t.goto(-75, -75)
t.pendown
t.color("red")
for i in range(100):
    t.forward (100 + i)
    t.right(72 +1)
turtle.exitonclick()