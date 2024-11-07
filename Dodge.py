# Section 1 - Setup
import codesters, random
from codesters import StageClass

stage = StageClass()

stage.set_background("flowers")
player = codesters.Sprite("flower")
player.set_size(1)
player.go_to(0,-200)
stage.disable_floor()


gameOver = False
lives = 5


# Section 2 - Objects


def falling_object():
    global gameOver
    if not gameOver:
        x_position = random.randint(-250,250)
        object = codesters.Sprite("sodacan", x_position, 250)
        object.set_size(0.4)
        object.set_y_speed(-10)
   
stage.event_interval(falling_object, 1)


# Section 3 - Collision


def collision( player, s2):
    global lives, gameOver
   
    if s2.get_image_name() == "sodacan":
        stage.remove_sprite(s2)
        if lives == 0:
            gameOver= True
            player.say("Game Over")
        else:
            lives -= 1
            
             
player.event_collision(collision)




# Section 4 - Controls

def move_left(sprite):
    if lives > 0:
        sprite.move_left(8)



def move_right(sprite): 
    if lives > 0:   
	    sprite.move_right(8)

player.event_key("left", move_left)
player.event_key("right", move_right)

