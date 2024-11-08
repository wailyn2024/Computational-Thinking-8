# Section 1: Setup
import codesters
from codesters import StageClass
stage = StageClass()

stage.set_background("canvas")
s1 = codesters.Sprite("mouse_cursor",0,0)
s1.set_size(0.09)

#Define actions
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

def blue_pen(sprite):
	sprite.set_color("blue")

def yellow_pen(sprite):
	sprite.set_color("gold")
	
def black_pen(sprite):
	sprite.set_color("black")
#movement def
def move_up(sprite):
	sprite.move_up(1)
   	 
def move_down(sprite):
	sprite.move_down(1)
    
def move_left(sprite):
	sprite.move_left(1)
    
def move_right(sprite):    
	sprite.move_right(1)
#Binding
s1.event_key("j",draw)
s1.event_key("k",stop_drawing)
s1.event_key("i",erase)
s1.event_key("9",red_pen)
s1.event_key("8",green_pen)
s1.event_key("7",blue_pen)
s1.event_key("6",yellow_pen)
s1.event_key("5",black_pen)


#movement binding
s1.event_key("w", move_up)
s1.event_key("s", move_down)
s1.event_key("a", move_left)
s1.event_key("d", move_right)

#push
print("Canvas is set up. Go to PORTS to begin drawing.")
print("Colors are as such-")
print("9- red, 8- green, 7- blue, 6- yellow, 5- black.")
print("j to begin drawing, k to stop, i to erase. WASD for movement.")