# Section 1: Setup
import codesters
from codesters import StageClass
stage = StageClass()

stage.set_background("basment")
s1 = codesters.Sprite("plauge", 0, -200)
s1.set_size(0.1)
s2 = codesters.Sprite("child")

# Section 2: define controls
def move_up(sprite):
    sprite.move_up(0.8)


def move_down(sprite):
    sprite.move_down(0.8)


def move_left(sprite):
    sprite.move_left(0.8)


def move_right(sprite):
    sprite.move_right(0.8)
# Section 3: define hide and show


def hide(sprite):
    sprite.hide()


def show(sprite):
    sprite.show()


def pen(sprite):
    sprite.pen_down()

# Section 4: bind controls to specific keys
s1.event_key("up", move_up)
s1.event_key("down", move_down)
s1.event_key("left", move_left)
s1.event_key("right", move_right)
s2.event_key("w", move_up)
s2.event_key("a", move_down)
s2.event_key("s", move_left)
s2.event_key("d", move_right)
s1.event_key("q", pen)
