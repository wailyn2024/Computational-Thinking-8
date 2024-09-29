# ###############################################
# ### SETUP ###
import turtle
# ###############################################

t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("black")
t.pendown()
for i in range(10):
    for i in range(5):
        t.forward(10)
        t.left(90)
    t.penup()
    t.left(90)
    t.forward(20)
# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################
