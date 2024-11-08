# Section 1 - Setup
import codesters
import random
from codesters import StageClass
stage = StageClass()

player = codesters.Sprite("space_ship")
player.set_size(0.05)
player.go_to(0, 0)
stage.disable_floor()
stage.set_background("space")

gameOver = False
lives = 5
value = [0.2,0.1,0.4,]
value2 = [-5, -8, -4]
value3 = [5, 8, 4]
# Section 2 - Objects


def falling_object():
	global gameOver
	if not gameOver:
		options = random.randint(1,4)

		match options:
			case 1:
				y_position = random.randint(-250,250)
				object = codesters.Sprite("meteor", y_position, 250)
				object.set_size(random.choice(value))
				object.set_y_speed(random.choice(value2))

			case 2:
				y_position = random.randint(-250, 250)
				object = codesters.Sprite("meteor", 250, y_position)
				object.set_size(random.choice(value))
				object.set_x_speed(random.choice(value2))

			case 3:
				y_position = random.randint(-250, 250)
				object = codesters.Sprite("meteor", y_position, -250)
				object.set_size(random.choice(value))
				object.set_y_speed(random.choice(value3))

			case 4:
				y_position = random.randint(-250, 250)
				object = codesters.Sprite("meteor", -250, y_position)
				object.set_size(random.choice(value))
				object.set_x_speed(random.choice(value3))
    
stage.event_interval(falling_object, 0.5)
g = 0
h = 0
# Section 3 - Collision

def collision(s1, s2):
	global lives, gameOver,g,h
    
	if s2.get_image_name() == "meteor":
		stage.remove_sprite(s2)
		if lives == 0:
			gameOver = True
			player.say("GameOver", 0.5)
		else:
			v = random.randint(1,2)
			lives-=1
			player.say("lives =" + str(lives))
			if v == 1:
				h += 0.1
			elif v == 2:
				g += 0.1


player.event_collision(collision)

# Section 4 - Controls
def left(sprite):
	heading = sprite.heading
	sprite.set_heading(heading + 1 + g)
def right(sprite):
	
	heading = sprite.heading
	sprite.set_heading(heading - 1 - h)
def forward(sprite):
	sprite.forward(2)


player.event_key("a", left)
player.event_key("d", right)
player.event_key("w", forward)


