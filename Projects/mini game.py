# Section 1: Setup
import codesters
import math
from codesters import StageClass
stage = StageClass()

stage.set_background("park")
s1 = codesters.Sprite("person1",0,-200)
s1.set_size(0.5)
s2 = codesters.Sprite("person2",0, 200)
s2.set_size(0.5)



# Section 2: define controls
def move_up(sprite):
	sprite.move_up(2)
   	 
def move_down(sprite):
	sprite.move_down(2)
    
def move_left(sprite):
	sprite.move_left(2)
    
def move_right(sprite):    
	sprite.move_right(2)




# Section 3: define hide and show
def show(sprite):
	sprite.show()

def hide(sprite):
	sprite.hide()

def turn_left(sprite):
	heading = sprite.heading
	sprite.set_heading(heading + 1)

def turn_right(sprite):
	heading = sprite.heading
	sprite.set_heading(heading - 1)

def forward(sprite):
	sprite.forward(1)

def draw(sprite):
	sprite.pen_down()


def stop_drawing(sprite):
	sprite.pen_up()


def erase(sprite):
	sprite.pen_clear()


def red_pen(sprite):
	sprite.set_color("red")


def green_pen(sprite):
	sprite.set_color("green")


def reset(sprite):
	s1.goto(0,-200)
	s2.goto(0,200)


def find(sprite):
	x1 = s2.get_x()
	y1 = s2.get_y()
	x2 = s2.get_x()
	y2 = s2.get_y()
	distance = math.sqrt((x2-x1)**2+(y2-y2)**2)
	if distance < 100:

		s1.say("I win")



# Section 4: bind controls to specific keys
s1.event_key("w", move_up)
s1.event_key("s", move_down)
s1.event_key("a", move_left)
s1.event_key("d", move_right)
s2.event_key("up", move_up)
s2.event_key("down", move_down)
s2.event_key("left", move_left)
s2.event_key("right", move_right)
s1.event_key("q", draw)
s2.event_key("m", hide)
s2.event_key("n", show)
s1.event_key("e", erase)
s1.event_key("r", reset)
s2.event_key("r", reset)
s2.event_key("t", find)


# Section 5: reminder message
print("Game has started. Open the screen using PORTS to play")