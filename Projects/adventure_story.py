# intro
print("You are outside walking your dog. It's 9:15 in late november, and its dark and cold.")
print("You are lost, so you find an abandoned house and lead him inside, but he runs off. You dont think much of it, because he's a dog.")
print("after about 45 minutes, you start to get worried,he's been gone for awhile.")
print("Goal: Get out of the house safely before its to late...")

# choice 1
c1 = input("Do you go upstairs, or to the living room?")
if "stairs" in c1:
    print("You head up the stairs")

    # choice 2
    print("You walk upstairs and hear faint dripping")
    c2 = input("Do you go to the bathroom or the bedroom?")
    if "bedroom" in c2:
        print("You slowly walk towards the bedroom, and creak open the door...")
         # choice 4
        print("You walk into the bedroom and see a vent (about 3 by 3 feet; its huge), a closet, and a chest of drawers ")
        c4 = input("Which one do you pick to examine first?")
        if "vent" in c4:
            print("You walk towards the vent, half opened")
            print("You open up the vent grate. Like 3 6 feet down, then theres a stop. You decide immediately to go in")
            print("You slide in and crawl through it. All of a sudden, your leg gets caught in one of the grates")
            print("You wont be able to get out without some help. Your all alone.")
            print("Mission Failed")
        elif "closet" in c4:
            print("You tiptoe over to the closet, and the dripping gets closer")
            print("You open it up to see your dog, upside down, hung. Suddenly, someone comes up from behind you and puts a cloth soaked in chloroform over your mouth and nose. You pass out.")
            print("Mission Failed")
        else:
            print("You open up the top drawer and find a old key. Engraved on the key, it says shed")
            print("You walk downstairs and grab a flashlight to go to the shed")  
            # choice 9
            c9 = input("This is your last chance. Do you go outside or into the bathroom instead?")
            if "outside" in c9:
                print("You grab your boots and step outside into the cold crisp november air.")
                print("You scan your eyes for a shed, and see the faint outline in the distance.")
                print("As you walk out there, you can here faint whining. You approach the door,and unlock it")
                print("You open the door and see your dog there. He is alive, but it looks like his leg is broken.")
                # choice 10
                c10 = input("Do you carry him out or leave him to go grab a splint?")
                if "leave" in c10 or "splint" in c10:
                    print("You run back to the house to grab a splint.")
                    print("As you grab the splint, you see your dog walk back to the house, perfectly fine.")
                    print("You put away the splint and quickly grab your dog to leave the house")
                    print("You walk away from the house with your dog, and find another family that will house you for the night")
                    print("As you fall asleep in this sweet old womans house, you realize that this dog doesn't have the same birthmark as your real dog.")
                    print("That isn't your dog...")
                    print("Mission Semi-Success.")
            else:
                print("You head up to the bathroom, but as you walk in, a poisonous gas fills your lungs, and drop to the ground")
                print("Mission Failed")       

    else:
        print("You walk over the the bathroom and slowly open the door...") 
        print("A poisonous gas flows out and you breath it in. You slowly die from the fumes ")
        print("Mission Failed")   

else:
    print("You go towards the living room")
    # choice 3
    print("When you get into the living room, you dont see anything, but hear faint whining")
    c3 = input("Do you investigate the whining, or go to the basement instead, where you hear faint footsteps?")
    if "investigate" in c3 or "whining" in c3:
        print("You go closer towards the whining, near the sliding door.")
        # choice 6
        print("You look out the window and see a faint shadow of an animal. It could be your dog. You go outside an the whining gets closer")
        print("By now you're terrified, but the animal hasn't moved yet")

    else:
        print("You tiptoe over towards the basement door. But its closed...")
        # choice 5
        print("You go to the kitchen cupboard and grab the key, turing around and going back to the basement door.")
        print("You open up the door to reveal an old creaky door with an ominous sign.")
        print("Beware, for all who shall come,die.")
        c5 = input("Do you unlock the door and go downstairs or go grab a bat or a flashlight first?")
        if "unlock" in c5 or "door" in c5 or "downstairs" in c5:
            print("You unlock the door and are met with an old creaky staircase, with an ominous lightbulb at the very bottom. You continue down.")
            print("As soon as you get to the bottom step, a figure in runs at you and stabs your throat.The last think you see is your dog, hung by its throat")
            print("Mission Failed")

        else:
            print("You go to grab a bat or a flashlight")
            # choice 7
            print("You go to the kitchen and open up a drawer. You can only carry a flashlight or a bat. ")
            c7 = input("Do you pick a flashlight or a bat?")
            if "flashlight" in c7:
                print("You grab the flashlight and creak down the stairs. With the light, you can see where you are heading.")
                # choice 8
                print ("A figure steps close towards you. You point the light at it but all you see is a black figure. You start to run away, but the figure grabs your body. You break free.")
                c8 = input("Do you try and fight the figure, or run away?")
                if "fight" in c8 or "figure" in c8:
                    print("You hit him in the face and it lets out a frill shriek.")
                    print("He pushes you up against the wall by your neck, and you slowly loose consciousness.")
                    print("Th last thing you see is your dog, hanging by its neck, blood dripping down his body, dead.")
                    print ("Mission failed")

                else:
                    print("You sprint up the stairs and out of the house. You continue running until you cant anymore. You made it out, but your dog didn't")
                    print("Oh well")
                    print("Mission Success!")

            else:
                print("You grab the bat and slowly creak down the stairs. You loose your footing and fall down, down, down.")
                print("You die from brain damage")
                print("Mission Failed")