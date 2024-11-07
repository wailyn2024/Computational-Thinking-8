# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()
stage.set_background("park")
s1 = codesters.Sprite("turtle")
s1.set_size(0.2)
s1.go_to(0,-200)
stage.disable_floor()

gameOver = False
lives = 5

# Section 2 - Objects

def falling_object():
	global gameOver
	if not gameOver:
		x_position = random.randint(-250,250)
		object = codesters.Sprite("soccerball", x_position, 250)
		object.set_size(0.4)
		object.set_y_speed(-10)
    
stage.event_interval(falling_object, 0.5)

# Section 3 - Collision

def collision(s1, object):
	global lives, gameOver
    
	if object.get_image_name() == "soccerball":
		stage.remove_sprite(object)
		if lives == 0:
			print("game over")
			gameOver = True
		else:
			print("running out of lives")
			lives-=1
         	 
s1.event_collision(collision)


# Section 4 - Controls
def move_up(s1):
    s1.move_up(1)
     
def move_down(s1):
    s1.move_down(1)
    
def move_left(s1):
    s1.move_left(1)
    
def move_right(s1):    
    s1.move_right(1)

def turn_left(s1):
    heading = s1.heading
    s1.set_heading(heading + 1)

def turn_right(s1):
    heading = s1.heading
    s1.set_heading(heading - 1)


s1.event_key("w", move_up)
s1.event_key("s", move_down)
s1.event_key("a", move_left)
s1.event_key("d", move_right)