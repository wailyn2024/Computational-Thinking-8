import turtle

t = turtle.Turtle()
turtle.penup()
t.goto(-100, -100)
t.color("cyan")
t.pendown()

for i in range(6):
    t.forward(100)
    t.pendown()