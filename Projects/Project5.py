# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()

stage.set_background("winter")
player = codesters.Sprite("apple")
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
        object = codesters.Sprite("baseball", x_position, 250)
        object.set_size(0.4)
        object.set_y_speed(-5)
   
stage.event_interval(falling_object, 0.5)


# Section 3 - Collision


def collision(s1, s2):
    global lives, gameOver
   
    if s2.get_image_name() == "baseball":
        stage.remove_sprite(s2)
        if lives == 0:
            gameOver = True
        else:
            lives -= 1


             
player.event_collision(collision)




# Section 4 - Controls

def move_up(sprite):
	sprite.move_up(5)
   	 
def move_down(sprite):
	sprite.move_down(5)
    
def move_left(sprite):
	sprite.move_left(5)
    
def move_right(sprite):    
	sprite.move_right(5)


player.event_key("w", move_up)
player.event_key("s", move_down)
player.event_key("a", move_left)
player.event_key("d", move_right)