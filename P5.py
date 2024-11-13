# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()

player = codesters.Sprite("corgi")
player.set_size(0.4)
player.go_to(0,-200)
stage.disable_floor()
stage.set_background("fall")

gameOver = False
time = 60
lives = 4

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
		lives -= 1
		if lives <= 0:
			player.say("You Lose:(")
			gameOver = True
			sprite = codesters.Sprite("download")
			sprite.set_size(2)
		else:
			player.say("you lost a life")
			
         	 
player.event_collision(collision)


# Section 4 - Controls
def move_left(sprite):
	sprite.move_left(4)
    
def move_right(sprite):    
	sprite.move_right(4)

player.event_key("a", move_left)
player.event_key("d", move_right)