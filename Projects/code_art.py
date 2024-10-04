import turtle,random

t = turtle.Turtle()

t.penup()
t.goto(-150, 0)
t.pendown()
t.speed(100)

#shape1
turtle.bgcolor("MidnightBlue")
colors = ["Coral", "OrangeRed"]
for i in range(400):
    t.color(colors[ i % 2 ] )
    t.forward(240 + i%70)
    t.left(182)

turtle.exitonclick()