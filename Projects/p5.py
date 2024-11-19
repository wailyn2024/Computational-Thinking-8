#section 1 - setup
import codesters
from codesters import StageClass
stage = StageClass()
import random
gameOver = False
lives = 20
#section 2 objects

player = codesters.Sprite("sailboat")
player.set_size(0.2)
player.go_to(0,-200)
stage.disable_floor()
stage.set_background("water")

def falling_object():
	global gameOver
	if not gameOver:
		x_position = random.randint(-250,250)
	object = codesters.Sprite("fish", x_position, 250)
	object.set_size(0.4)
	object.set_y_speed(-5)
    
stage.event_interval(falling_object, 0.5)

# Section 3 - Collision
def hide(sprite):
	sprite.hide()

def collision(player, object):
	global lives, gameOver

	
	if object.get_image_name() == "fish":
		stage.remove_sprite(object)
		
		if lives <= 0:
			print("game over")
			gameOver = True
			hide.s2
			hide.s1
		else:
			print("you have {lives} live(s) left")
		lives += -1
player.event_collision(collision)



# Section 4 - Controls
def move_left(sprite):
	player.move_left(6)
def move_right(sprite):    
	player.move_right(6)

player.event_key("a, left",move_left)
player.event_key("d, right",move_right)








