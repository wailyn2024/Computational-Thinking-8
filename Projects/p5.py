# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()


#todo
# change what the player looks like
# add a background, the command is stage.set_background("name of background")
# adding messages when you get hit with player.say("message")

player = codesters.Sprite("bat")
player.set_size(0.2)
player.go_to(0,-200)
stage.disable_floor()
stage.set_background("fall")

gameOver = False
lives = 5

# Section 2 - Objects

def falling_object():
	global gameOver
	if not gameOver:
		x_position = random.randint(-250,250)
		object = codesters.Sprite("applecore", x_position, 250)
		object.set_size(0.4)
		object.set_y_speed(-10)
    
stage.event_interval(falling_object, 0.5)

# Section 3 - Collision

def collision(player, object):
	global lives, gameOver
    
	if object.get_image_name() == "applecore":
		stage.remove_sprite(object)
		if lives == 0:  
			print("test")
			gameOver=True
			player.say("you lose!")
		else:
			print("test")
			lives-=1
			
         	 
player.event_collision(collision)


# Section 4 - Controls
# need to add a control to move left and right

def move_up(sprite):
	sprite.move_up(1)
   	 
def move_down(sprite):
	sprite.move_down(1)

def move_left(sprite):
	sprite.move_left(1)

def move_right(sprite):
	sprite.move_right(1)

player.event_key("w", move_up)
player.event_key("s", move_down)
player.event_key("a", move_left)
player.event_key("d",move_right)