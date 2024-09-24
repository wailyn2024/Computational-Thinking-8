###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
# Intro
print("you walk onto the old creepy boat")
print("the old floorboards of the boat creak under your feet as you walk inside")
print("")
print ("will you look for the treasure rumored to be hidden in this old boat?")
print("-----------------------------")


# choice 1
c1 = input ("do you choose to search in the [boats basement] or the [captains quarters]?")
if "boats basement" in c1:
    print("the old stairs break and you drown to death...")
else:
    print("the door to the captains quarters opens and you see the dark gloomy room full of chests!") 


