# Section 1 - Setup
import codesters, random, time
from codesters import StageClass
stage = StageClass()

player = codesters.Sprite("PlayerCar")
player.set_size(0.1)
player.go_to(0,-200)
stage.disable_floor()
stage.set_background("road")

gameOver = False
lives = 5
speed = 1
points = 0

counter = 0
# Section 2 - Objects

def falling_object():
	global gameOver
	if not gameOver:
		x_position = random.randint(-250,250)
		object = codesters.Sprite("EnemyCar", x_position, 250)
		object.set_size(0.2)
		object.set_y_speed(-1 * speed)
    

def gain_points():
	global points
	global speed
	points += speed

def speedlimiter():
	global speed
	if speed > 15:
		speed = 15
	if speed < 1:
		speed = 1

def temp_event():
	global counter
	global speed
	gain_points()
	speedlimiter()
	counter+=1
	if counter == 3:
		falling_object()
		counter=0


stage.event_interval(temp_event, 1)
# Section 3 - Collision

def collision(player, object):
	global lives, gameOver
	
	if object.get_image_name() == "EnemyCar":
		global points
		stage.remove_sprite(object)
		if lives == 0:
			player.say(f"*intense dying sounds*(you got {points}")
			time.sleep(4)
			gameOver = True
		else:
			lives -=1
    	      
player.event_collision(collision)


# Section 4 - Controls
def move_left():
    player.move_left(5)

def move_right():
    player.move_right(5)

def accelerate():
	global speed
	speed += 1
	player.say(f"your speed: {speed}")
	time.sleep(0.5)
def brake():
	global speed
	speed -= 1
	player.say(f"your speed: {speed}")
	time.sleep(0.5)


player.event_key("left", move_left)
player.event_key("right", move_right)
player.event_key("up", accelerate)
player.event_key("down", brake)
player.event_key("a", move_left)
player.event_key("d", move_right)
player.event_key("w", accelerate)
player.event_key("s", brake)