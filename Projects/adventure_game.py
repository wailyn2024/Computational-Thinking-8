#setup
import time
#intro
print("you wake up in teh middle of nowhere.")
print("the sun is setting and it will be night in about 5 minutes.")
print("you look around and see a cave, a forest, and the beach")
#choice 1
c1 = input("Where do you want to go? ")
#cave
if "cave" in c1.lower():
    print(" ")
    print("you walk into the cave and feel like your being watched")
    print("as you turn around the silhouette of creature and then nothing")
    print("game over")
    #forest
elif "forest" in c1.lower():
    print(" ")
    print("you wander through the forest and see a hut, and a long winding path")
    forestc1 = input("where do you go next? ")
    #hut
    if "hut" in forestc1.lower():
        print(" ")
        print("you walk into the hut and see that its a mess almost like someone was in a hurry to get out of there")
        print("as it turns to night you hear a loud noise outside")
        hutc1 = input("do you go investigate? ")
        if "yes" in hutc1.lower():
            print(" ")
            print("as you go out to investigate the door slams shut behind you")
            print("as you turn around...")
            print("game over")
        else:
            print(" ")
            print("you decide to stay in the hut")
            print("eventually you collapse into a deep sleep and wake up to the sound of birds in the background")
            print("you head outside and see a road that you could've sworn wasn't there before")
            print("as you walk down the road you see a sign pointing into the woods that say one mile ahead")
            print("however you also see a sign pointing farther down the road that says that a town is 2 miles that way")
            roadc1 = input("do you go down the road or into the forest? ")
            #road
            if "road" in roadc1.lower():
                print(" ")
                print("as you walk down the road a car comes into view")
                print("the car stops near you and offers you one supply")
                print("they have food, water, and gas")
                roadc2 = input("what do you take? ")
                if "food" in roadc2.lower() or "water" in roadc2.lower():
                    print(" ")
                    print("you thank the driver for the supplies and they give you a smile and say anytime")
                    print("with your new supply you feel nourished and ready to walk to the town")
                    print("however you eventually collapse")
                    print("dont take food from strangers")
                    print("game over")
                elif "gas" in roadc2.lower():
                    print(" ")
                    print("you thank the driver for the supplies and they look almost disapointed")
                    print("as you walk down the road you come across an abandoned car")
                    print("good thing you took the gasoline")
                    print("you are able to get the car started and drive to the town")
                    print("congrats you win")
                else:
                    print(" ")
                    print("you decide not to take anything from the stranger")
                    print("as you walk down the road you pass an abandoned vehicle which is out of gas")
                    print("too bad you didn't take the gas")
                    print("as you walk down the road it seems like its stretching out longer and longer")
                    print("you eventually collapse")
                    print("i guess that sign was wrong")
                    print("game over")
            else:
                print(" ")
                print("you end up going into the forest")
                print("as you head into the forest the trail starts to wind and split")
                print("eventually the trail comes to a stop right back where it started")
                print("you decide to walk down the road instead but as soon as you take a step on the trail in the direction of the road its almost like you walk right back into the forest")
                print("as you desperately try to find a way off the trail you eventually collapse from exhaustion")
                print("game over")
    #path
    elif "path" in forestc1.lower():
        print(" ")
        print("as you walk along the path and it turns to night")
        print("you start to hear rustling in the bushes and a loud screech coming from the direction of the earlier cave")
        print("you start to run but trip on a root as you get up you feel a sharp pain the back of your head")
        print("game over")
    else:
        (" ")
        print("you end up wandering the forest some more and end up completely lost")
        print("as it turn to night you hear a screech coming from the direction of the cave and start running")
        print("you manage to find a bush to hide in...")
        print("the screeches slowly get closer almost as if it saw which direction you were going")
        print("as it gets farther into the night you collapse into a sleep but wake up to a loud breathing behind you in the middle of the night")
        print("game over")
#beach
else:
    print(" ")
    print("you go to the beach")
    print("as you walk along the beach you see a ship in the distance")
    print("the ship seems to be a small rowboat")
    beachc1 = input("do you call out to it? ")
    if "yes" in beachc1.lower():
        print(" ")
        print("there is no response just an eery silence")
        beachc2 = input("do you want to swim or keep walking down the beach? ")
        if "swim" in beachc2.lower():
            print(" ")
            print("as you swim out to the rowboat it seem almost as if its slowly drifting away")
            print("suddenly you get pulled under the wave right when it seems like you are finally making progress")
            print("game over")
        elif "walking" in beachc2.lower():
            print("")
            print("as you walk down the beach you come across a motorboat seemingly with no owner in sight")
            print("you take the motorboat and find a map in the storage you are able to make your way to civilization")
            print("congratulations you made it out")
        else:
            print("")
            print("you decide to stay put and as the night slowly creeps over the island you hear a screech coming from the direction of the cave")
            print("as you turn to look at the direction of the screech all you see is darkness")
            print("game over")
    else:
        print("")
        print("you keep walking down the beach and come across an abandoned motorboat")
        print("you take the motorboat and find a map in the storage you are able to make your way to civilization")
        print("congratulations you made it out")








