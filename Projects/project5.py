# Section 1 - Setup
import codesters, random 
from codesters import StageClass
stage = StageClass ()
stage.set_background("barn")

player = codesters.Sprite("kitten")
player.set_size(0.5)
player.go_to(0,-200)
stage.disable_floor()

gameOver = False
lives = 1

# Section 2 - Objects

def falling_object():
	global gameOver
	if not gameOver :
		x_position = random.randint(-250,250)
		object = codesters.Sprite("milkjug", x_position, 250)
		object.set_size(0.4)
		object.set_y_speed(2)
    
stage.event_interval(falling_object, 0.5)

# Section 3 - Collision

def collision(player, object):
	global lives, gameOver
    
	if object.get_image_name() == "milkjug":
		lives -= 1
		stage.remove_sprite(player)
		if lives == 0:
			print("test")
			gameOver=True
		else:
			print("test")
         	 
player.event_collision(collision)


# Section 4 - Controls
def move_up(sprite):
	sprite.move_up(1)
def move_down(sprite):
	sprite.move_down(1)
def move_left(sprite):
	sprite.move_left(1)
def move_right(sprite):    
	sprite.move_right(1)
player.event_key("up", move_up)
player.event_key("down", move_down)
player.event_key("left", move_left)
player.event_key("right", move_right)
def turn_left(sprite):
	heading = sprite.heading
	sprite.set_heading(heading + 1)

def turn_right(sprite):
	heading = sprite.heading
	sprite.set_heading(heading - 1)

