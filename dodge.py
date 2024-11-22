# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()


player = codesters.Sprite("basket")
player.set_size(0.2)
player.go_to(0,-200)
stage.disable_floor()
stage.set_background("spring")


gameOver = False
points = 0


# Section 2 - Objects


def falling_object():
    global gameOver
    if not gameOver:
        x_position = random.randint(-250,250)
        object = codesters.Sprite("flowers", x_position, 250)
        object.set_size(0.4)
        object.set_y_speed(-10)
   
stage.event_interval(falling_object, 0.5)


# Section 3 - Collision


def collision(s1, s2):
    global lives, gameOver
   
    if s2.get_image_name() == "flowers":
        stage.remove_sprite(s2)
        if points == 0:
            print("Catch the flowers in the bag!")
        else:
            print("Keep going!")
            points+=1

            if points == 5:
                 gameOver = True
             
player.event_collision(collision)


# Section 4 - Controls
def move_left(sprite):
	sprite.move_left(1)
    
def move_right(sprite):    
	sprite.move_right(1)
player.event_key("d", move_right)
player.event_key("a", move_left)
