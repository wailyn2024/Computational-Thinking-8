###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
Flower = stage.set_background ("flowers")

Pink = codesters.Square (-100, 100, -100, 'Pink')
Lavender = codesters.Square (200, -200, 200, 'Lavender')
Blue = codesters.Square (100, -100, 100, 'Blue')
LightYellow = codesters.Square ( , 255, 224, 'Light Yellow')
                        
Cardinal = codesters.Sprite ("cardinal", -100, 100)
Cardinal.set_size(0.1)
Flower2 = codesters.Sprite ("Flower", 200, -200)
Flower2.set_size(0.1)
Sprite = codesters.Sprite ("sprite", 100, -100)
Sprite.set_size(0.1)
Dog = codesters.Sprite ("dog", 100, -100)
Dog.set_size (0.1)

message1 = codesters.Text ("Eva",0,220,"red")
message2 = codesters.Text ("Never wake me up before you go go",0,-220,"black")