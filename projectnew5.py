# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()
stage.set_background("moon")


player = codesters.Sprite("fish")
player.set_size(0.6)
player.go_to(0,-200)
stage.disable_floor()


gameOver = False
lives = 5
points = 0


# Section 2 - Objects


def falling_object():
    global gameOver
    if not gameOver:
        x_position = random.randint(-250,250)
        object = codesters.Sprite("soccerball", x_position, 250)
        object.set_size(0.4)
        object.set_y_speed(-7)
        
        
        x_position = random.randint(-250,250)
        object = codesters.Sprite("dog", x_position, 250)
        object.set_size(0.1)
        object.set_y_speed(-6)


   
stage.event_interval(falling_object, 0.5)


# Section 3 - Collision


def collision(s1, s2):
    global lives, gameOver, points
   
    if s2.get_image_name() == "soccerball":
        stage.remove_sprite(s2)
        if lives == 0:
            gameOver = True
        else:
            lives -=1
            
            
    if s2.get_image_name() == "dog":
        stage.remove_sprite(s2)
        if points == 5:
            gameOver = True
            player.say("win")
        else:
            points +=1

             
player.event_collision(collision)

def move_up(fish):
	fish.move_up(2)
	
def move_down(fish):
	fish.move_down(2)

def move_right(fish):
	fish.move_right(2)

def move_left(fish):
	fish.move_left(2)



# Section 4 - Controls

player.event_key("up", move_up)
player.event_key("down", move_down)

# Section 5: bind controls to specific keys
player.event_key("left", move_left)
player.event_key("right", move_right)

