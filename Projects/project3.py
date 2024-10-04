import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's position and color
t.goto(100, 0)
t.color('cyan')

# Draw a 5-sided star
for i in range(5):
    t.forward(180)
    t.left(72)

# Keep the turtle window open until clicked
turtle.exitonclick()