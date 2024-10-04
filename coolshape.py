import turtle,random

t = turtle.Turtle()

t.penup()
t.goto(100, 0)
t.pendown()
t.speed(100)

turtle.bgcolor("DeepPink")
colors=["Slate Blue","Crimson"]
for i in range (200):
    t.color (random.choice(colors))
    t.forward(100 + i%50)
    t.left(200)

t.penup
t.goto(100,0)
t.pendown()

r = turtle.Turtle()

r.penup()
r.goto(-100,-40)
r.pendown()
r.speed(100)


colors=["orange","yellow"]
for i in range (90):
    r.color(random.choice(colors))
    r.forward(40+i%30)
    r.left(400)

r.penup()
r.goto(100,-40)
r.pendown()
r.speed(100)

turtle.exitonclick()