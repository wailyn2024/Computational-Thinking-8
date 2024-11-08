# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()


player = codesters.Sprite("turtle")
player.set_size(0.2)
player.go_to(0,-200) 
stage.disable_floor()
stage.set_background("TrumpFace")

gameOver = False
lives = 5


# Section 2 - Objects


def falling_object1():
    global gameOver
    if not gameOver:
        x_position = random.randint(-240,240)
        object = codesters.Sprite("Handcuff", x_position, 250)
        object.set_size(0.35)
        object.set_y_speed(-12)
       
   

def falling_object2():
    global gameOver
    if not gameOver:
        x_position = random.randint(-250,250)
        object = codesters.Sprite("MoneyBag", x_position, 250)
        object.set_size(0.30)
        object.set_y_speed(10)
       

def temp():
    r = random.randint(1,10)
    if r < 5:
        falling_object1()
    if r > 8:
        falling_object2()


stage.event_interval(temp,1)


# Section 3 - Collision


def collision(s1, s2):
    global lives, gameOver
   
    if s2.get_image_name() == "Handcuff":
        stage.remove_sprite(s2)
        if lives == 0:
            player.say("GAMEOVER")

            gameOver = True
        else:
            print("test_handcuff")
            lives-=1
            
   
    if s2.get_image_name() == "MoneyBag":
        stage.remove_sprite(s2)
        if lives == 0:
            player.say("GAMEOVER")

            gameOver = True
        else:
            print("test")
            lives+=1
             
player.event_collision(collision)




# Section 4 - Controls
def move_right(player):
    player. move_right(10)

player.event_key("d", move_right)

def move_left(player):
    player. move_left(10)

player.event_key("a", move_left)

