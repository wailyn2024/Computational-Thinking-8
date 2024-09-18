###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background ("image.png")

q1 = codesters.Square(100, 100, 200,'LightCoral')
q2 = codesters.Square(-100, 100, 200,'MediumAquamarine')
q3 = codesters.Square(-100, -100, 200,'Violet')
q4 = codesters.Square(100, -100, 200,'Gold')

s1 = codesters.Sprite("kitten.gif", 100, 100)
s2 = codesters.Sprite("flowers.gif", 100, -100)
s2.set_size(1.3)
s3 = codesters.Sprite("paint pallet.png", -100, 100)
s3.set_size(0.1)
s4 = codesters.Sprite("st,small,507x507-pad,600x600,f8f8f8.psd", -100, -100)
s4.set_size(0.3)


message1 = codesters.Text("My name is Emimae Yamada-Morigeau",0,220,"LightSkyBlue")
message2 = codesters.Text("This is my code of arms! ",0,-200,"LightSkyBlue")