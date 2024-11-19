# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()
stage.set_background("fall")

s1 = player = codesters.Sprite("hoop",0,-200)
player.set_size(0.6)
player.go_to(0,0)
stage.disable_floor()

gameOver = False
points = 0


# Section 2 - Objects


def falling_object():
    global gameOver
    if not gameOver:
        x_pos = random.randint(-250,250)
        object = codesters.Sprite("basketball", x_pos, 250)
        object.set_size(0.5)
        object.set_y_speed(2)
   
stage.event_interval(falling_object, 0.5)


# Section 3 - Collision


def collision(s1, s2):
    global points, gameOver
   
    if s2.get_image_name() == "basketball":
        points += 1
        stage.remove_sprite(s2)
        if points == 30:
            gameOver = True
            player.say("You did it!You won!",2)
             
player.event_collision(collision)




# Section 4 - Controls

def move_up(sprite):
	sprite.move_up(8)
   	 
def move_down(sprite):
	sprite.move_down(8)
    
def move_left(sprite):
	sprite.move_left(8)
    
def move_right(sprite):    
	sprite.move_right(8)

s1.event_key("w", move_up)
s1.event_key("s", move_down)
s1.event_key("a", move_left)
s1.event_key("d", move_right)