# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()


player = codesters.Sprite("turtle")
player.set_size(0.2)
player.go_to(0,-200)
stage.disable_floor()


gameOver = False
lives = 5

stage.set_background("rainbow")
s1 = codesters.Sprite("person1",0,-200)
s1.set_size(0.5)

# Section 2 - Objects


def falling_object():
    global gameOver
    if not gameOver:
        x_position = random.randint(-250,250)
        object = codesters.Sprite("bat", x_position, 250)
        object.set_size(0.2)
        object.set_y_speed(10)
   
stage.event_interval(falling_object, 0.5)

# Section 3 - Collision


def collision(s1, s2):
    global lives, gameOver
   
    if s2.get_image_name() == "bat":
        stage.remove_sprite(s2)
        if lives == 0:
            s1.say("Game Over")
            gameOver = True
        else:
            lives -= 1
            s1.say("ow",1)

            gameOver = False 
    # else: 
    #       print ("") 
    #       lives -=1
s1.event_collision(collision)



# Section 4 - Controls


def move_up(sprite):
	sprite.move_up(5)
   	 
def move_down(sprite):
	sprite.move_down(5)
    
def move_left(sprite):
	sprite.move_left(5)
    
def move_right(sprite):    
	sprite.move_right(5)

s1.event_key("w", move_up)
s1.event_key("s", move_down)

s1.event_key("d", move_right)
s1.event_key("a", move_left)

