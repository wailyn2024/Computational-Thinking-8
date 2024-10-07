# ###############################################
# ### SETUP ###
import turtle
# ###############################################

t = turtle.Turtle()
t.penup()
t.goto(-500, -100)
t.color("red")
t.pendown()

for i in range(10):
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.penup()
    t.forward(200)
    t.pendown()
#t.forward(100)



# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################
