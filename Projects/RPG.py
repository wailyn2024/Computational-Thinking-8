import random
#opening
print("welcome to the job")
print("hope you have a great time at freddy fazbears's pizzeria")
Question = input("You got a message, do you want to open it?")
if "yes" or "ok" in Question:
    print("INFO FOR YOUR FIRST DAY, the animatronics tend to move at night, make sure to watch for them.")
    print("")
    print("your a little worried but fine otherwise.")
else:
    print("you ignore the message")

#Introducing
print("A bit later you get to the pizzeria")
print("")
print("the door opens with a shake.")
print("")
print("as you search the pizzeria, you see 3 bipedal animal suits")
print("")
print("The first is a 9 foot tall chicken, with a orange beak and a cupcake (chica)")
print("")
print("The second is a 10 foot tall fox, with giant hook on its left hand, looking like if you touch it it would hurt.(foxy)")
print("")
print("The third is a 9 foot tall bunny, who has a rock guitar.(bonnie)")
#VARS
LDoorClosed = False
RDoorClosed = False
Game = True
time = 20
night = 1
power = 100
BonnieMove = 0
ChicaMove = 0
FreddyMove = 0
FoxyMove = 0
FoxyStage = 0
BonnieAggro = 0
ChicaAggro = 0
FreddyAgro = 0
FoxyAgro = 0
BonnieRoom = 0
ChicaRoom = 0
#Night setup
while Game:
    if time <= 0:
        night += 1
        time = 20
        LDoorClosed = False
        RDoorClosed = False
        BonnieRoom = 0
        ChicaRoom = 0
        FoxyStage = 0
        print("its night "+str(night)+"!")
        power = 100
    if night == 1:
        BonnieAggro = 3
    if night == 2:
        BonnieAggro = 5
        FoxyAgro = 2
        ChicaAggro = 3
    if night == 3:
        BonnieAggro = 7
        FoxyAgro = 4
        ChicaAggro = 6
    if night == 4:
        BonnieAggro = 9
        FoxyAgro = 6
        ChicaAggro = 8
    if night == 5:
        BonnieAggro = 13
        FoxyAgro = 12
        ChicaAggro = 11
    if night == 6:
        print("you win")
        Game = False
        quit
    #text
    if ChicaRoom == 3:
        print("You hear a sound in the kitchen")
    print(f"you have {power}")
    print("")
    print("you can close or open a door, check cams or wait")
    print("")
    MoveMade = input("What are you gonna do")
    if "close" in MoveMade:
        Question = input("left or right door")
        if "left" in Question:
            print("left door closed")
            LDoorClosed = True
        else:
            print("Right door closed")
            RDoorClosed = True
            
    elif "open" in MoveMade:
        Question = input("left or right door")
        if "left" in Question:
            print("left door opened")
            LDoorClosed = False
        else:
            print("Right door opened")
            RDoorClosed = False
    elif "wait" in MoveMade:
        print("You wait")
        time -= 1
        power += 2
    elif "cams" in MoveMade:
        power -= 5
        print("there is main room, Left hallway, Right hallway and pirates cove.")
        Question = input("Which one do you look at?")
        if "main" in Question:
            if BonnieRoom == 0:
                print("The bunny is standing on the left stage.")
            if ChicaRoom == 0:
                print("The chicken is standing on the right of the stage.")
        if "right" in Question:
            if BonnieRoom == 3:
                print("The bunny peeks into the right hallway")
            else:
                print("nothing here")
        if "left" in Question:
            if ChicaRoom == 3:
                print("The chicken stands in the left hallway")
            else:
                print("nothing here")
        if "cove" in Question:
            print("foxy is at stage "+str(FoxyStage)+".")
    #Power management
    if LDoorClosed:
        power -= 5
    if RDoorClosed:
        power -= 5
    #animatronics moving
    BonnieMove = random.randint(1,20)
    if BonnieMove <= BonnieAggro:
        BonnieRoom += 1
    ChicaMove = random.randint(1,20)
    if BonnieMove <= ChicaAggro:
        ChicaRoom += 1
    FoxyMove = random.randint(1,20)
    if FoxyMove <= FoxyAgro:
        FoxyStage += 1
    #bonnnie
    if BonnieRoom == 5 and not LDoorClosed:
        print("You hear a sound to your left, as you attempt to close the door, the purple bunny appears.")
        print("game over.")
        Game = False
        quit
    elif BonnieRoom == 5 and LDoorClosed:
        BonnieRoom = 1 
        print("bonnie doesn't get in from the right door, it storms away")
    #chica
    if ChicaRoom == 5 and not RDoorClosed:
        print("A sound crashes in, and the yellow chicken runs into your room.")
        print("game over.")
        Game = False
        quit
    elif ChicaRoom == 5 and RDoorClosed:
        ChicaRoom = 0
        print("Chica doesnt get in from the right door, it storms away")
    #freddy
    if power <= 0:
        print("suddenly, the power goes out, your doors open.")
        print("you hear the sound of a musicbox, and a evil laugh.")
        print("nothing happens, as you go to reach for the door, a huge bear roars at you, and grabs at you")
        print("game over")
        Game = False 
        quit
    #foxy
    if FoxyStage >= 5 and not LDoorClosed:
        print("You hear thundering footsteps, and the fox dashes into your room.")
        print("game over")
        Game = False
        quit
    elif FoxyStage >= 5 and LDoorClosed:
        print("foxy charges down the hallway and hits the door, its sprints away.")
        FoxyStage = 1
    if not Game:
        quit
        print("")
        print("game over, try again")