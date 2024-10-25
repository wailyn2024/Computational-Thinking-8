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
def show (sprite):
	sprite.show()

# Section 4: bind controls to specific keys
s1.event_key("w", move_up)
s1.event_key("s", move_down)
s1.event_key("a", move_left)
s1.event_key("d",move_right)
s1.event_key("h",hide)
s1.event_key("g", show)

# Section 5 more left and right and forward
def turn_left(sprite):
	heading = sprite.heading
	sprite.set_heading(heading + 1)
	s1.event_key("b", turn_left)

def turn_right(sprite):
	heading = sprite.heading
	sprite.set_heading(heading - 1)
s1.event_key("m", turn_right)

def forward(sprite):
	sprite.forward(1)
s1.event_key("t", forward)

#Section 8 draw

def draw(sprite):
	sprite.pen_down()
s1.event_key("z", draw)

def stop_drawing(sprite):
	sprite.pen_up()
s1.event_key("y", stop_drawing)

def erase(sprite):
	sprite.pen_clear()
s1.event_key("q", erase)

def red_pen(sprite):
	sprite.set_color("red")
s1.event_key("v", red_pen)

def green_pen(sprite):
	sprite.set_color("green")
s1.event_key("l", green_pen)

# Section 7: reminder message
print("Game has started. Open the screen using PORTS to play")