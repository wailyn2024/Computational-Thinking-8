# Section 1: Setup
import codesters
from codesters import StageClass
stage = StageClass()

t = codesters.Sprite("turtle")
def move_up(sprite):
    sprite.move_up(10)
t.event_key("up",move_up)

def move_down(sprite):
    sprite.move_down(10)
t.event_key("down",move_down)

def move_left(sprite):
    sprite.move_left(10)
t.event_key("left",move_left)

def move_right(sprite):
    sprite.move_right(10)
t.event_key("right",move_right)

stage.set_background("drawbridge")

def hide (sprite):
    sprite.hide ()
t.event_key("h", hide)

def show (sprite):
    sprite.show ()
t.event_key("s",show)

