import turtle

t = turtle.Turtle()
t.color("cyan")
t.speed(10)

t.penup()
t.goto(0, 0)
t.pendown()

for i in range(8):
    t.forward(100)
    t.left(135)

t.begin_fill()
t.color("magenta")
t.end_fill()

t.penup()
t.hideturtle()
turtle.done()
