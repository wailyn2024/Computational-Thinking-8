# Section 1: Setup
import codesters
from codesters import StageClass
stage = StageClass()

s1 = codesters.Sprite("mouse_cursor",0,0)
s1.set_size(0.09)
stage.set_background("canvas")

s2 = codesters.Sprite("real_mouse", 10, 10)
s2.set_size(0.09)

#Movement and actions s1
def move_up(s1):
	s1.move_up(1)
   	 
def move_down(s1):
	s1.move_down(1)
    
def move_left(s1):
	s1.move_left(1)
    
def move_right(s1):    
	s1.move_right(1)
	
def draw(s1):
	s1.pen_down()

def polo():
	if
#binding s1
s1.event_key("up", move_up)
s1.event_key("down", move_down)
s1.event_key("left", move_left)
s1.event_key("right", move_right)
s1.event_key("q",draw)

#Movement and actions def s2
def move_up(s2):
	s2.move_up(1)
   	 
def move_down(s2):
	s2.move_down(1)
    
def move_left(s2):
	s2.move_left(1)
    
def move_right(s2):    
	s2.move_right(1)

def hide(s2):
	s2.hide()
	
def show(s2):
	s2.show()

def reset():
	s2.go_to(90,90)
	s1.go_to(-90,-90)
#Binding actions s2
s2.event_key("w", move_up)
s2.event_key("s", move_down)
s2.event_key("a", move_left)
s2.event_key("d", move_right)
s2.event_key("m", hide)
s2.event_key("n", show)
s2.event_key("r", reset)