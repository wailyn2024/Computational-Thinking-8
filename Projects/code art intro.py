# ###############################################
# ### SETUP ###
import turtle
# ###############################################

# color and speed
import turtle, random, math
t = turtle.Turtle()
t.speed(250000)
turtle.bgcolor("white")

# sure its centered
t.penup()
t.goto(0,-250)
t.pendown()

# making the circles 18 times
for i in range  (18):

    colors = ["blue", "red", "purple"]
    for i in range (100):
        t.color(random.choice(colors))
        t.forward(75)
        t.left(random.choice([60+5]))
    t.penup()
    t.forward(75)
    t.pendown()


turtle.exitonclick()