# ###############################################
# ### SETUP ###
import turtle
# ###############################################




t = turtle.Turtle()
t.speed(110)
t.penup()
t.goto(0,0)
t.pendown()
colors = ["lavender", "Thistle", "plum","MediumPurple","MediumSlateBlue"]
for i in range(1000):
    t.color( colors[i%5])
    t.forward(10 + i)
    t.left(120)

#color changing spiral
t = turtle.Turtle()
t.speed(110)
t.penup()
t.goto(0,0)
t.pendown()
colors = ["blue","teal","indigo","cyan"]
for i in range (1000):
    t.color( colors[i%4])
    t.forward(10)
    t.left(61 + i)


#SPIRAL TWO, OTHER DIRECTION
t = turtle.Turtle()
t.speed(110)
t.setheading(0)
t.penup()
t.goto(0,0)
t.pendown()

colors = ["blue","teal","indigo","cyan"]
for i in range (1000):
    t.color( colors[i%4])
    t.forward(10)
    t.left(122 + i)
#SPIRAL 3
t = turtle.Turtle()
t.speed(110)
t.setheading(0)
t.penup()
t.goto(0,0)
t.pendown()

colors = ["blue","teal","indigo","cyan"]
for i in range (1000):
    t.color( colors[i%4])
    t.forward(10)
    t.left(-122 + i)
#SPIRAL 4
t = turtle.Turtle()
t.speed(110)
t.setheading(0)
t.penup()
t.goto(0,0)
t.pendown()
colors = ["blue","teal","indigo","cyan"]

for i in range (1000):
    t.color( colors[i%4])
    t.forward(10)
    t.left(-61 + i)

#DO NOT TOUCH
######ENDING####
#################
#############
