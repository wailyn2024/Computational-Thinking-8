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


# Section 3: define hide and show
def hide(sprite):
	sprite.hide()
s1.event_key("q", hide)

def show(sprite):
	sprite.show()
s1.event_key("h", show)

# Section 4: bind controls to specific keys
s1.event_key("up", move_up)
s1.event_key("down", move_down)

# Section 5: bind controls to specific keys
s1.event_key("left", move_left)
s1.event_key("right", move_right)

# Section 6: reminder message
print("Game has started. Open the screen using PORTS to play")

def move_up(turtle):
	turtle.move_up(1)
	
def move_down(turtle):
	turtle.move_down(1)

def move_right(turtle):
	turtle.move_right(1)

def move_left(turtle):
	turtle.move_left(1)


s1.event_key("w", move_up)
s1.event_key("s", move_down)

# Section 5: bind controls to specific keys
s1.event_key("a", move_left)
s1.event_key("d", move_right)



