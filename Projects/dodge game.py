# Section 1 - Setup
import codesters, random
from codesters import StageClass

from Maze import move_left, move_right
stage = StageClass()
stage.set_background("image copy.png")


s1 = codesters.Sprite("kitten.gif")
s1.set_size(0.7)
s1.go_to(0,-200)
stage.disable_floor()
print ("lives")

gameOver = False
lives = 5


# Section 2 - Objects


def falling_object():
    global gameOver
    if not gameOver:
        x_position = random.randint(-250,250)
        object = codesters.Sprite("flowers", x_position, 260)
        object.set_size(1.0)
        object.set_y_speed(11)
   
stage.event_interval(falling_object, 2.0)


# Section 3 - Collision


def collision(s1, s2):
    global lives, gameOver
    
    if s2.get_image_name() == "flowers":
        stage.remove_sprite(s2)
        if lives == 0:
            s1.say("Game over!!!")
            gameOver=True
        else:
            print("")
            lives-=1
            s1.say(f"{lives} lives")
         

    
s1.event_collision(collision)




# Section 4 - Controls(sprite):
def move_up(sprite):
   	 sprite.move_left(1)
def move_down(sprite):
	sprite.move_right(1)


s1.event_key("right",move_right)
s1.event_key("left",move_left)