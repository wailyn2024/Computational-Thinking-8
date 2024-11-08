# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()
import time
##
print("Game started. Go to PORTS to play.")
print("Use arrow keys to move.")
player = codesters.Sprite("white_man")
player.set_size(0.9)
player.go_to(0,-200)
stage.disable_floor()
stage.set_background("irs")
gameOver = False
lives = 10

player.say("Uh oh! I have to pay my taxes.")
player.say("Quick! Help me evade taxes!")
# Section 2 - Objects

def falling_object():
	global gameOver
	if not gameOver:
		x_position = random.randint(-250,250)
		object = codesters.Sprite("money", x_position, 500)
		object.set_size(0.2)
		object.set_y_speed(1)
	if gameOver:
		object.show = False

stage.event_interval(falling_object, 9)

# Section 3 - Collision
def collision(Player, money):
	global lives, gameOver
	
	if money.get_image_name() == "money":
		stage.remove_sprite(money)
		if lives == 0:
			player.say("OOH NO, THE TAX COLLECTERS")
			police = codesters.Sprite("popo")
			police.set_size(0.2)
			police.go_to(200,0)
			time.sleep(1.5)
			gameOver = True
		else:
			lives -= 1
			player.say(f"Ouchie! I can only evade taxes {lives} more times!")
    	      
player.event_collision(collision)


# Section 4 - Controls

def move_left(player):
	player.move_left(5)
    
def move_right(player):    
	player.move_right(5)


player.event_key("left", move_left)
player.event_key("right", move_right)

