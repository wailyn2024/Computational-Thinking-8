#Intro
print("You walk into the hunted mansion.")
print("The door loudly creaks and shuts behind you.")
print("")
print("Will you ever be able to find the golden tressure?")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#choice 1
c1=input("Do you choose to go the [elevator] or into the [garage]")
if "elevator" in c1:
    print("You queitly walk into the elevator")
#choice 2
print("You take the elevator to the 3rd floor, the hallway goes left to the master bedroom and right to the bathroom.")
c2=input("Do you go [left] or [right?]")
if "left" in c2 or "bedroom" in c2:
    print("You walk left towards the master bedroom.")
    print("When you walk into the master bedroom you find alot of maps laying on the bed")
    print("You pocket the maps just in case if you need them later")
elif"bathroom"in c2:
    print("You walk right toawrds the bathroom.")
    print("In the bathroom, you can choose to check the [sink cabinets] or the [towel cupboard]")
    c2=input("What do you check")
    if "sink cabinets" in c2:
        print("You open the sink cabinets...")
        print("In the sink cabinets you find the golden tressure box but no tressure...")
        print("You wonder is anyone else here...?")
    elif "towel cupboard" in c2:
        print("you look in towel cupboard")
        print("You find nothing in the towel cupboard")
        

    else:
        print("You decide to go into the garage.")
    #choice 3
    print("In the garage, you can choose to investigate the [boxes],the [storage cabinets] or the [old rug]")
    c3=input("What do you investigate?")
    if "box" in c3:
        print("You open the boxes....")
        print("When you open the boxes you find old dusty toys")
    elif"storage cabinets" in c3:
        print("You walk towards the storage cabinets.....")
        print("You walk towards the storage cabinets but when you walk you feel the old rug move under you feet")
        print("So you decide to check the old rug")
    else:
        print("You drag the old rug away and it reveals the trap door....")
    #this is the scary part...
    #choice 4
    print("You see the trap door, do you decide you [investigate] it or [keep looking around the house]?")
    c4=input("What do you investigate?")
    if "investigate" in c4:
        print("When you open the trap door it reavels a staircase")
    elif"you keep looking around the house" in c4:
        print("When you are walking around the house you hear the front door slam shut") 
        print("You have a feeling you aren't you only person in the house....")
    #choice 5
    print("Do you decide to go [down the stairs] of the trap door or do you go to see [who else is in the house]?")
    c5=input("What do you choose to investigate?")
    if "down the stairs" in c5:
        print("when you do down the stairs you find just find random stuff around a desk")
    elif"who else is in the house" in c5:
        print("When you are looking around the house you keep seeing footprints...")
    #choice 6
    print("The footprints lead you outside and the door locks shut... [game over] or [restart]")
    c6=input("What do you choose to do?")
    if "game over" in c6:
    print("Game over")
    else:"restart" in c6:
    print("Restart")

