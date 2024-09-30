# ###############################################
# ### SETUP ###
import turtle
# ###############################################




t = turtle.Turtle()
t.speed(110)
t.penup()
t.goto(0,0)
t.pendown()
color = ["lavender", "Thistle", "plum","MediumPurple","MediumSlateBlue"]
for i in range(1000):
    t.color(color%5)
    t.forward(10 + i)
    t.left(120)

#color changing spiral
t = turtle.Turtle()
t.speed(110)
t.penup()
t.goto(0,0)
t.pendown()
colors = ["blue", "teal", "indigo", "cyan"]
for i in range (1000):
    t.color( colors[i%4])
    t.forward(10)
    t.left(61 + i)



#DO NOT TOUCH
######ENDING####
#################
t.exitonclick()
#############
