# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()
stage.set_background("fall")
player = codesters.Sprite("baseball")
player.set_size(1)
player.go_to(9,-200)
stage.disable_floor()

gameOver = False
lives = 3

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

def collision(player, object):
	global lives, gameOver
    
	if object.get_image_name() == "soccerball":
		stage.remove_sprite(object)
		if lives == 0:
			player.say("Game Over!")
			gameOver = True
		else:
			lives -= 1
			player.say("You have been hit!")
         	 
player.event_collision(collision)


# Section 4 - Controls

def move_left(sprite):
	player.move_left(1)
    
def move_right(sprite):    
	player.move_right(1)
player.event_key("right", move_right)
player.event_key("left", move_left )
