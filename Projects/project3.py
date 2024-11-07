import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's position and color to pink
t.goto(100, 0)
t.color('pink')

# Draw a 5-sided star
for i in range(5):
    t.forward(180)
    t.left(72)
