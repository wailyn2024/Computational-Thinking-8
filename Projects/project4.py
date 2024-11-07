# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()


player = codesters.Sprite("character1.gif")
player.set_size(0.4)
player.go_to(0,-200)
stage.disable_floor()
stage.set_background("winter.png")


gameOver = False
lives = 5


# Section 2 - Objects


def falling_object():
    global gameOver
    if not gameOver:
        x_position = random.randint(-250,250)
        object = codesters.Sprite("soccerball", x_position, 250)
        object.set_size(0.4)
        object.set_y_speed(-10)
   
stage.event_interval(falling_object, 0.5)


# Section 3 - Collision


def collision(s1, s2):
    global lives, gameOver
   
    if s2.get_image_name() == "soccerball":
        stage.remove_sprite(s2)
        if lives == 0:
            print("game over")
            gameOver = True


        else:
            print("lose one life")
            lives-= 1
        
             
player.event_collision(collision)




# Section 4 - Controls
def move_left(sprite):
	sprite.move_left(5)
    
def move_right(sprite):    
	sprite.move_right(5)
player.event_key("a", move_left)
player.event_key("d", move_right)