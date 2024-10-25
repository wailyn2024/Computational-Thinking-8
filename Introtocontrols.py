# Section 1: Setup 
import codesters 
from codesters import StageClass 
stage = StageClass()

stage.set_background("moon")
s1 = codesters.Sprite("person1",0,-200)
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

def show(sprite):
    sprite.show()  

# Section 3: define hide and show 
def hide (sprite) : 
    sprite.hide()

# Section 4: turning and moving forward 
def turn_left(sprite):
    heading = sprite.heading 
    sprite.set_heading(heading + 1)

def turn_right(sprite):
    heading = sprite.heading 
    sprite.set_heading(heading + 1)

def forward(sprite):
    sprite.forward(1)

# Section 5: bind controls to specific keys 
s1.event_key("w", move_up)
s1.event_key("s", move_down)
s1.event_key("a", move_left)
s1.event_key("d", move_right)
s1.event_key("h", hide)
s1.event_key("g", show)
s1.event_key("e", turn_left)
s1.event_key("z", turn_right)
s1.event_key("r", forward)

# Section 6: reminder message 
print("Game has started. Open the screen using PORTS to play.")