# Intro 
print("You walk into the forest.")
print("You hear a loud crack.")
print("You are looking for lost treasure you heard about in a book.")
print("Will you ever be able to find it while staying alive?")

# choice 1
c1 = input("you see a fork in the path do you go [right] or [left]?")
if "right" in c1:
    print("you head down the right path.")

    # choice 2 
    print("Halfway down the left path there is a tall tree with a large hole.")
    c2 = input("Do you go inside the [hole] in the tree or do you go [around] the tree?")
    if "hole" in c2:
        print("You go inside the hole in the tree.")
        print("On the inside of the tree there is a magic portal do you go [inside] the portal or do you [leave] the forest?")
        #choice 3
        c3 = input("Where do you go?")
        if "inside" in c3: 
            print("You walk inside the magic portal carefully")
            print("You feel the magic of the portal as you step through sinking through you")
            print("When you open your eyes on the other side of the portal you see a dark field and automatically die from death of a terrifying creature.")
        else: 
            print("You leave the forest and go home.")
    else: 
        print("You walk around the tree and keep going down the path.")
        print("At the end of the path there is a giant killer shrew that kills you.")

# choice 4 
else: 
    print("You head down the left path.")
    print("Down at the end of the left path there is a wide cave, on either side of the cave there is a fork in the road heading left and right.")
    print("Do you chose to go inside the [cave] or do you go [left] on the path or [right] on the path.")
    c4 = input("where do you go?")
    if "cave" in c4: 
        print("You enter the cave...")
        # choice 5 
        print("In the cave all you can see is darkness do you go on [without] a light or grab a match from your back pocket and find a stick to make a [torch]?")
        c5 = input("what do you do?") 
        if "without" in c5: 
            print("You walk blindly forward and trip on a stick, falling landing on a rock and dying.")
        else:
            print("You drop to your knees feeling out for a stick and find one right in front of you, lighting your torch.")
            print("Now that you have light you see 2 caves going off of the main cave")
           #choice 6
            print("Do you go down the[left] cave or the [right] cave?")
            c6 = input ("which way do you go?")
            if "left" in c5:
                print("You head down the left side of the cave, it ends at a steep drop off you don't see which causes you to fall and die.") 
            else:
                print("At the end of the right path you find a treasure chest full of money! You Win!")
    elif "left" in c4: 
        print("You walk down the left path...")
        c7 = input ("the left path ends in a dead end.")
    else:
        print("you head down the right path...")
        c8 = input ("at the end of the right path you come out at the entrance to the forest.")
