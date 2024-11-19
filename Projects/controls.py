# Section 1: Setup
from turtle import pendown
import codesters
from codesters import StageClass

import sprite
stage = StageClass()

stage.set_background("fall")
s1 = codesters.Sprite("p",0,-200)
s1.set_size(0.5)



# Section 2: define controls
def move_up(sprite):
	sprite.move_up(1)
   	 
def move_down(sprite):
	sprite.move_down(1)
    
def move_left(sprite):
	sprite.move_left(1)
    
def move_right(sprite):    
	sprite.move_right(1)

def draw (sprite):
	sprite.pen_down()
sprite.event_key("q", pendown)

# Section 3: define hide and show
def hide(sprite):
	sprite.hide()


# Section 4: bind controls to specific keys
s1.event_key("w", move_up)
s1.event_key("s", move_down)
s1.event_key("a", move_left)
s1.event_key("d", move_right)
s1.event_key("q", pendown)
# Section 5: reminder message
print("Game has started. Open the screen using PORTS to play")
