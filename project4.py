# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()

s1 = codesters.Sprite("shrew")
s1.set_size(0.09)
s1.go_to(0,-200)
stage.disable_floor()

gameOver = False
lives = 5

# Section 2 - Objects

def falling_object():
	global gameOver
	if not gameOver:
		x_position = random.randint(-250,250)
		object = codesters.Sprite("pogostick",0,1000)
							
		object.set_size(0.1)
		object.goto(x_position, 250)
		object.set_y_speed(-1)

stage.event_interval(falling_object, 8)

# Section 3 - Collision

def collision(s1, s2):
	global lives, gameOver
	
	if s2.get_image_name() == "pogostick":
		stage.remove_sprite(s2)
		if lives == 0:
			gameOver = True
		else:
			lives -= 1 
    	    
s1.event_collision(collision)

# Section 4 - Controls

def move_left(sprite):
    sprite.move_left(5)

def move_right(sprite):
    sprite.move_right(5)

def move_up(sprite):
    sprite.move_up(5)

def move_down(sprite):
    sprite.move_down(5)

s1.event_key("left", move_left)
s1.event_key("right", move_right)
s1.event_key("up", move_up)
s1.event_key("down", move_down)


