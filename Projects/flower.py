import turtle

# Function to draw a petal
def draw_petal(t):
    t.color("pink")  # Petal color changed to pink
    t.begin_fill()
    t.left(45)
    t.forward(100)
    t.circle(50, 90)
    t.left(90)
    t.circle(50, 90)
    t.forward(100)
    t.end_fill()
    t.right(135)

# Function to draw the hibiscus flower
def draw_hibiscus(t):
    for _ in range(5):  # Draw 5 petals
        draw_petal(t)
        t.right(72)  # Petal separation

# Function to draw the center of the flower
def draw_center(t):
    t.penup()
    t.goto(0, -20)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(20)  # Draw the center circle
    t.end_fill()

# Setup turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(10)

# Draw the hibiscus flower
draw_hibiscus(t)
draw_center(t)

# Finish drawing
t.hideturtle()
screen.mainloop()  # Keep the window open until closed