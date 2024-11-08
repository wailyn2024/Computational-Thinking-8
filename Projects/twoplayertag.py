# Section 1: Setup
import codesters
from codesters import StageClass
stage = StageClass()

#stage.set_background("moon")
s1 = codesters.Sprite("cat",0,-200)
s1.set_size(0.2)
s2 = codesters.Sprite("dog",0,200)
s2.set_size(0.2)



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
def hide(sprite):
    sprite.hide()
def show(sprite):
	sprite.show()
def reset(sprite):
	sprite.goto(0,-200)
def reset2(sprite):
	sprite.goto(0,200)
def tag(sprite):
	if s1.distance(s2.get_x(),)
	sprite.say(TAG!!!!)
	





# Section 3: define hide and show


# Section 4: bind controls to specific keys
s1.event_key("w", move_up)
s1.event_key("s", move_down)
s1.event_key("a",move_left)
s1.event_key("d", move_right)
s1.event_key("q", draw)
s1.event_key("r", reset)

s2.event_key("up", move_up)
s2.event_key("down", move_down)
s2.event_key("left",move_left)
s2.event_key("right", move_right)
s2.event_key("q", draw)
s2.event_key_press("m", hide)
s2.event_key_release("m", show)
s2.event_key("r", reset2)


# Section 5: reminder message
print("Game has started. Open the screen using PORTS to play")