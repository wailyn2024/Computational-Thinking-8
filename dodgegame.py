#Section 1 - Setup 
import codesters, random 
from codesters import StageClass 
stage= StageClass()
stage.disable_floor()
player= codesters. Sprite ("dog")

stage.set_background("park")
object_speed= 2
lives= 3

#Section 2- objects 
def falling_object(): 
    global object_speed, lives
    if lives >0: 
      x= random.randint (-250, 250)
      y= random.randint (-250, 250)
      object= codesters.Sprite ("ball", x, y)
    
      object. set_y_speed( object_speed)
stage. event_interval(falling_object, 2) 

# #Section 3- Collision 
def collision (player, object):
  global lives 

  if object.get_image_name()== "ball":
    stage.remove_sprite(object)
    lives=-1
    if lives== 0:
        player.say (f"Out of lives- you lose!", 5)
    else:
        player.say (f"{lives} lives", 0.5)



player.event_collision (collision)
#Section 4- controls 
def go_right():
   player.move_right(10)

player.event_key("right", go_right)

def go_left():
   player.move_left(10)

player.event_key("left", go_left)
  



