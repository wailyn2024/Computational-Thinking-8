# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()
stage.set_background("soccerfield")

player = codesters.Sprite("turtle")
player.set_size(0.2)
player.go_to(0,-200)
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
		object.set_y_speed(-15)
    
stage.event_interval(falling_object, 0.5)

# Section 3 - Collision

def collision(s1, s2):
	global lives, gameOver
    
	if s2.get_image_name() == "soccerball":
		stage.remove_sprite(s2)
		if lives == 0: 
			player.say("Game over")
			gameOver=True
		else:
			player.say("Lose live")
			lives-=1  
player.event_collision(collision)


# Section 4 - Controls

def move_left(sprite):
	sprite.move_left(3)

def move_right(sprite):    
	sprite.move_right(3)

# Section 5 - Controls

player.event_key("left", move_left )
player.event_key("right", move_right)