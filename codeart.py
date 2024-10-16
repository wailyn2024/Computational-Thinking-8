import turtle
#pink shape
t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("pink")
turtle.bgcolor("black")
t.pendown()

for i in range (6):
    t.forward(100)
    t.left(60)

for i in range (30):
    t.forward(160)
    t.left(100 +1)
#red shape
t = turtle.Turtle()
t.penup()
t.goto(-10, -100)
t.color("red")
t.pendown()

for i in range (3):
    t.forward(100)
    t.left(120)
for i in range (30):
    t.forward(160)
    t.left(120 +1)
#end
turtle.exitonclick()
