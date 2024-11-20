# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()


player = codesters.Sprite("cat")
player.set_size(0.2)
player.go_to(0,-200)
stage.disable_floor()
stage.set_background ("summer")


gameOver = False
lives = 3


# Section 2 - Objects


def falling_object():
    global gameOver
    if not gameOver:
        x_position = random.randint(-250,250)
        object = codesters.Sprite("fish", x_position, 250)
        object.set_size(0.5)
        object.set_y_speed(-1)
   
stage.event_interval(falling_object, 0.99)


# Section 3 - Collision


def collision(s1, s2):
    global lives, gameOver
   
    if s2.get_image_name() == "fish":
        stage.remove_sprite(s2)
        if lives == 0 :
            print("you lost!")
            player.say("you lost!")
            gameOver = True
        else:
           print("you got hit!")
           player.say("you got hit!")
           lives -= 1
        
             
player.event_collision(collision)




# Section 4 - Controls

def move_up(sprite):
    sprite.move_up(1)
     
def move_down(sprite):
    sprite.move_down(1)


player.event_key("f", move_up)
player.event_key("s", move_down)

def move_left(sprite):
     sprite.move_left(5)  

def move_right(sprite):
    sprite.move_right(3)
player.event_key("w", move_left)
player.event_key("t", move_right)
