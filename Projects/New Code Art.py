# ###############################################
# ### SETUP ###
import turtle
import random
# ###############################################

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle object
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
t.width(2)  # Set the pen width

# Function to draw a crazy pattern
def draw_crazy_pattern():
    for i in range(200):
        # Randomly change the color
        t.color(random.random(), random.random(), random.random())
        
        # Draw a shape (circle or square) with a twist
        if i % 2 == 0:
            t.circle(i)
        else:
            for _ in range(4):
                t.forward(i)
                t.right(90)
        
        # Rotate the turtle to create a spiraling effect
        t.right(45)  # Change the angle for a different effect

# Draw the crazy pattern
draw_crazy_pattern()

# Hide the turtle and finish
t.hideturtle()

# Keep the window open until clicked
turtle.exitonclick()
# ###############################################
