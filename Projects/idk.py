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
     print("the door to the captains quarters opens and you see the dark gloomy room full of chests!")    
    # choice 2
c1 = input ("do you open the [small shiny chest] or the [big rusty chest]?")


if "small shiny chest" in c1:
    print("a booby trap catches you as you walk there and it cuts off your head...")
else: 
    print ("the chest creeks slowly open and inside it holds gold coins and precious gems")
print("the old stairs break and you drown to death...")


# choice 3
c1 = input ("")