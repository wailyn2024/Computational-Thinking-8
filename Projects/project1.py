###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
Flower = stage.set_background ("flowers")

Pink = codesters.Square (255, 192, 203, 'Pink')
Lavender = codesters.Square (230, 230, 250, 'Lavender')
Blue = codesters.Square (176, 224, 230, 'Blue')
LightYellow = codesters.Square (255, 255, 224, 'Light Yellow')
                        
Cardinal = codesters.Sprite ("cardinal", 100, 100)
Cardinal.set_size(0.5)
Sprite = codesters.Sprite ("sprite", -100, -100)
Sprite.set_size(0.5)
Dog = codesters.Sprite ("dog", 100, -100)
Dog.set_size (0.1)

message1 = codesters.Text ("Eva",0,220,"red")
message2 = codesters.Text ("Never wake me up before you go go",0,-220,"black")