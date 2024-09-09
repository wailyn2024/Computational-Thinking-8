###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("court")

s1 = codesters.Square(100, 100, 200, 'white')
s2 = codesters.Square(-100, 100, 200, 'black')
s3 = codesters.Square(-100, -100, 200, 'white')
s4 = codesters.Square(100, -100, 200, 'black')

s1.set_size(0.5)
s2.set_size(0.5)
s3.set_size(0.5)
s4.set_size(0.5)

text1 = codesters.Text("pete kicska")
text2 = codesters.Text("witawy")

text1 = 




