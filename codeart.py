import turtle, random

t = turtle.Turtle ()

t.goto(-100,-100)
turtle.bgcolor("White")

t.speed(100)
colors = ["DarkOrange","DarkCyan","LightSeaGreen"]

for i in range (100) :
    t.color(random.choice(colors))
    t.forward(100)
    t.left (45+ 1)

for i in range (150) :
    t.color("DarkOrange")
    t.forward ( 100 + i )
    t.left (45)
    


    turtle.exitonclick ()
