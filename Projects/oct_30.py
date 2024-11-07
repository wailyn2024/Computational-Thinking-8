import codesters

turtle = codesters.Sprite ("turtle")
def move_up(sprite):
    sprite.move_up(10)
turtle.event_key("up", move_up)

def move_down(sprite):
    sprite.move_down(10)
turtle.event_key("down", move_down)

def move_left(sprite):
    sprite.move_left(10)
turtle.event_key("left", move_left)

def move_right(sprite):
    sprite.move_right(10)
turtle.event_key("right", move_right)

def draw(sprite):
    sprite.pen_down()
turtle.event_key("q", draw)

def stop_drawing(sprite):
    sprite.pen_up()
turtle.event_key("k", stop_drawing)

def erase(sprite):
    sprite.pen_clear()
turtle.event_key("e", erase)