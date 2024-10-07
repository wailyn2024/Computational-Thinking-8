import turtle, random, math

t = turtle.Turtle()

t.goto(100, 0)

#speed and background
turtle.bgcolor("white")
t.speed(50)
t.goto(0,0)

#color changing
colors = ["pink", "purple", "blue"]
for i in range (400):
    t.color( colors[ i % 3 ])
    t.forward( 50 + 1 + i )
    t.left( 72 )
#rotating
    t.forward( 50 + 1 + i )
    t.left( 88 )

turtle.exitonclick()
