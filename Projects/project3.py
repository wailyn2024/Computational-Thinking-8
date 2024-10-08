import turtle,random, math
t = turtle.Turtle()

t.speed(150)
turtle.bgcolor("red")

colors = ["gray", "yellow", "purple", "white", "black"]
for i in range(100):
    t.color("blue")
    t.forward(50 + i)
    t.left(75)


for i in range(500):
    t.color(random.choice(colors))
    t.forward(100 + i%100)
    t.left(120)

colors2 = ["blue", "yellow", "red", "orange", "brown" ]
for i in range(250):
    t.goto(200,200)
    t.color( colors [ i % 3 ] )
    t.forward(70)
    t.left(175)
turtle.exitonclick()