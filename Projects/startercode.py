# Section 1: Setup
import codesters
from codesters import StageClass
stage = StageClass()

stage.set_background("aussie")
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



# Section 3: define hide and show
def hide(sprite):
	sprite.hide()


# Section 4: bind controls to specific keys
s1.event_key("w", move_up)
s1.event_key("s", move_down)

s1.event_key("a", move_right)
s1.event_key("a", move_left)


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
# Section 5: reminder message
print("Game has started. Open the screen using PORTS to play")

# Section 2: define controls
def move_up(bench):
	bench.move_up(1)
   	 
def move_down(bench):
	bench.move_down(1)
    
def move_left(bench):
	bench.move_left(1)
    
def move_right(bench):    
	bench.move_right(1)
	
def draw(bench):
	bench.pen_down()


def stop_drawing(bench):
	bench.pen_up()


def erase(bench):
	bench.pen_clear()


def red_pen(bench):
	bench.set_color("red")


def green_pen(bench):
	bench.set_color("green")



# Section 3: define hide and show
def hide(bench):
	bench.hide()


# Section 4: bind controls to specific keys
s1.event_key("w", move_up)
s1.event_key("s", move_down)

s1.event_key("a", move_right)
s1.event_key("a", move_left)


def draw(bench):
	bench.pen_down()
s1.event_key("z", draw)

def stop_drawing(bench):
	bench.pen_up()
s1.event_key("y", stop_drawing)

def erase(bench):
	bench.pen_clear()
s1.event_key("q", erase)

def red_pen(bench):
	bench.set_color("red")
s1.event_key("v", red_pen)

def green_pen(bench):
	bench.set_color("green")
s1.event_key("l", green_pen)
# Section 5: reminder message
print("Game has started. Open the screen using PORTS to play")