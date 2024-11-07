# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()


player = codesters.Sprite("hoop")
player.set_size(0.7)
player.go_to(0,-200)
stage.disable_floor()
stage.set_background("gym")


gameOver = False
score = 0


# Section 2 - Objects


def falling_object():
    global gameOver
    if not gameOver:
        x_position = random.randint(-250,250)
        object = codesters.Sprite("basketball", x_position, 250)
        object.set_size(0.7)
        object.set_y_speed(-6)
   
stage.event_interval(falling_object, 0.5)


# Section 3 - Collision


def collision(s1, s2):
    global score, gameOver
   
    if s2.get_image_name() == "basketball":
        stage.remove_sprite(s2)
        if score == 15:
            gameOver = True
            player.say("you win!")
        else:
            score+=1
            player.say("point",1)
             
player.event_collision(collision)




# Section 4 - Controls
def move_left(sprite):
    sprite.move_left(3)
    
def move_right(sprite):    
    sprite.move_right(3)
    
player.event_key("right", move_right)
player.event_key("left", move_left )