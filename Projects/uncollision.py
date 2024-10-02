import turtle
from random import shuffle

WIDTH, HEIGHT = 600, 500

INCREMENT = 50

TURTLE_WIDTH = 20

X, Y = 0, 1

def dot_round(x, base=INCREMENT):
    return int(base * round(float(x) / base))

turtle.setup(WIDTH, HEIGHT)

turtle.shape("turtle")

while True:
    positions = set()

    while True:

        position = (dot_round(turtle.xcor()), dot_round(turtle.ycor()))  # coerce position to grid

        if position in positions:
            break  # collision with line

        positions.add(position)

        turtle.setposition(position)  # coerce turtle back onto our grid

        moves = list(range(3))

        shuffle(moves)

        clone = None

        for move in moves:
            clone = turtle.clone()  # use an invisible clone to test the waters
            clone.hideturtle()
            clone.penup()

            if move == 1:
                clone.right(90)
            elif move == 2:
                clone.left(90)

            clone.forward(INCREMENT)

            position = (dot_round(clone.xcor()), dot_round(clone.ycor()))

            if position[X] <= TURTLE_WIDTH//2 - WIDTH//2 or position[X] > WIDTH//2 - TURTLE_WIDTH//2:
                continue  # avoid collision with wall

            if position[Y] <= TURTLE_WIDTH//2 - HEIGHT//2 or position[Y] > HEIGHT//2 - TURTLE_WIDTH//2:
                continue  # avoid collision with wall

            if position not in positions:
                break

        else:  # no break
            break  # accept the inevitable, there's no good move

        turtle.setheading(clone.heading())
        turtle.forward(INCREMENT)

    turtle.reset()

# close the turtle window to get out of this program