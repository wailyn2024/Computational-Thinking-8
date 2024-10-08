
import turtle,random,math
#turtlesetup
t = turtle.Turtle()
t.speed(200)
t.penup()
t.goto(-100, -100)
t.color("red")
t.pendown()
#turtlecolor
turtle.bgcolor("Blue")
colors = ["green", "Red"]
#turtledrawing
for i in range(100):
    t.color(random.choice(colors))
    t.forward(120 + i)
    t.left(72)

t.goto(-100,-100)
for i in range(120):
    t.color(random.choice(colors))
    t.forward(120 - i)
    t.left(72)

for i in range(100):
    r = 50
    t.circle(r + i)

for i in range(100):
    r = 50
    t.circle(r - i)
    t.circle(r + i)

t.goto(-100,-100)
for i in range(120):
    t.color(random.choice(colors))
    t.forward(120 - i)
    t.right(90)
t.goto(-100,-100)
for i in range(100):
    r = 41
    t.circle(r + i)
for i in range(100):
    r = 41
    t.circle(r - i)



# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################
