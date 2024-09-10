###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background ("spring")

q1=codesters.square(100,100,200,'Pink')
q2=codesters.square(100,100,200,'MistyRose')
q3=codesters.square(-100,-100,200,'Pink')
q4=codesters.square(100,-100,200,'MistyRose')

s1=codesters.sprite("Pink roses",100,100)
s1.set_size(0.5)
s2=codesters.sprite("Thomas",-100,-100)
s2.set_size(0.5)
s3=codesters.sprite("mountaaaane", 100,-100)
s3.set_(0.5)
s4=codesters.sprite("")