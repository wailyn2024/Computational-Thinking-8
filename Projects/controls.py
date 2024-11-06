# Section 1: Setup
import codesters
import math
from codesters import StageClass
stage = StageClass()

stage.set_background("park")
s1 = codesters.Sprite("person2",0,-200)
s2 = codesters.Sprite("person1" ,0,-100)
s1.set_size(0.5)
s2.set_size(0.5)



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
s2.event_key("m",hide)
def show(sprite):
	sprite.show()
s2.event_key("n", show)
#heading
def turn_left(sprite):
	heading = sprite.heading
	sprite.set_heading(heading + 1)

def turn_right(sprite):
	heading = sprite.heading
	sprite.set_heading(heading - 1)

def forward(sprite):
	sprite.forward(1)
	


# Section 4: bind controls to specific keys
s1.event_key("up", move_up)
s1.event_key("down", move_down)
s1.event_key("right", move_right)
s1.event_key("left", move_left )
s2.event_key("w", move_up)
s2.event_key("s", move_down)
s2.event_key("d", move_right)
s2.event_key("a", move_left )




#Section 5
def draw(sprite):
	sprite.pen_down()
s2.event_key("q",draw)


def stop_drawing(sprite):
	sprite.pen_up()
s1.event_key("e",stop_drawing)

def erase(sprite):
	sprite.pen_clear()
s1.event_key("x", erase)


def red_pen(sprite):
	sprite.set_color("red")
s1.event_key("z",red_pen)


def green_pen(sprite):
	sprite.set_color("green")
s1.event_key("c", green_pen)

def reset(sprite):
	s2.goto(100,200)
	s1.goto(99,100)
s1.event_key("r",reset)
s2.event_key("r", reset)

def talk(sprite):
	x1 = s2.get_x()
	y1 = s2.get_y()
	x2 = s2.get_x()
	y2 = s2.get_y()
	distance = math.sqrt((x2-x1)**2+(y2-y2)**2)
	if distance < 100:

		s2.say("I win")
s2.event_key("t", talk)
# Section 6: reminder message
print("Game has started. Open the screen using PORTS to play")
