import turtle
t = turtle.Turtle()

t.goto(100, 0)
#color change 
t.color("red")

for i in range (200):
    t.forward(100 + i)
    #switch direction
    t.left(72)


for i in range (200):
    t.forward(110 + i)
    t.left (90)


for i in range (300):
    t.speed(400 + i)
    #speedup
    t.left (88)




