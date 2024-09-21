#intro
print("You walk into your local mall")
print("You then realize that no one is there")
print("The door closes behind you and locks")
print("You here a growling noise coming from somewhere near by")
print("Can you survive the apocalypse and escape?")

#choice 1
c1= input("Do you ride the [elevator] or walk towards the [growling]?")
if "elevator" in c1:
    print("You press the button and enter the elevator")

else:
    print("You slowly walk towards the growling and a zombie bites you")

#choice 2
c2=input("You exit onto the fifth floor and see a long [hallway], do you walk down it or enter the room to your [right]?")
if "hallway" in c2:
    print("You walk down the hallway")
else:
    print("You enter the room and a zombie bites you on the arm")

#choice 3
c3=input ("As you walk down the hallway you see a bathroom where there is a hole cut in the floor where the tub should be. Do you go down the [hole], [explore] the bathroom, or find [another room]?")
if "hole" in c3:
    print("You crawl down the hole...")

    #choice 4
    c4=input ("you see a room with hundreds of things that were supposed to be stocked years ago. Do you [eat] something, or [escape] the room? ")
    if "eat" in c4:
        print("congratulations! you have built up an immunity to the zombies! you can escape. ")
    else:
        print("you continue walking around the room trying to find a way out, when a zombie comes out of a box and bites you on the arm.")

elif"explore" in c3:
    print("You start exploring the bathroom...")

    #choice 5
    c5=input ("you continue to look around the bathroom and find a small flask with a strange purple liquid that has been spilled on the floor. Do you slip the liquid into your [pocket], or [drink] it?")
    if "pocket" in c5:
        print("you slip the flask into your pocket and exit the bathroom.")

        #choice 7
        c7=input ("as you exit the bathroom you see the hallway your in splits off to the [left] or to the [right], which way do you go?")
        if "left" in c7:
            print("you turn left.")
        else:
            print("you turn right.")

    else:
        print("you drink the liquid and become violently ill, resulting in you becoming a zombie.")
            
        
else:
    print("You attempt to find another room...")

    #choice 6
    c6=input ("you continue walking down the hallway but a zombie rounds the corner a bites you on the arm ")