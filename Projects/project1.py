###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
#Flower = stage.set_background ("2flower.jpeg")

Pink = codesters.Triangle (-150, -150, 250, 'Pink')
Lavender = codesters.Square (250, 250, 250, 'Lavender')
Blue = codesters.Rectangle (-50, -50, -50, -100,'Blue')
LightYellow = codesters.Circle ( 100, 100, 100, 'Light Yellow')
                    
Cardinal = codesters.Sprite ("cardinal", -150, -150)
Cardinal.set_size(0.1)
Flower2 = codesters.Sprite ("flower", 150, 150)
Flower2.set_size(1)
Sprite = codesters.Sprite ("spritecan",-50, -50)
Sprite.set_size(0.15)
Dog = codesters.Sprite ("dog", 100,100)
Dog.set_size (0.1)

message1 = codesters.Text ("Eva",0,220,"red")
message2 = codesters.Text ("Never wake me up before you go go",0,-220,"black")