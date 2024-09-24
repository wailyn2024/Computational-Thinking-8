# Intro
print("The walk into the spooky abandoned school.")
print("The door creaks shut behind you.")
print("")
print("Will you ever be able to find your lost dog?")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# choice 1
c1 = input("Do you choose to go up the [stairs] or into the [basement]?")
if "stairs" in c1:
    print("You carefully walk up the stairs")
    c2 = input("The upstairs hallway goes left to the classrooms and right to the bathrooms")
    if "left" in c2 or "classrooms" in c2:
        print("You walk left towards the classrooms")
        c6 = input("You go to the classrooms and you can either investigate or run away")
        if "if run away" in c6:
            print("You can go to the basement")
        else:
            print("Run out the school and not find the dog")
else:
    print("You decide to go into the basement")
    c3 = input("The basement hallway goes left to chairs and closet and right to three rooms")
    if "right" in c3 or "three rooms" in c3:
        print("You walk right toward one of the classrooms")
        c4 = input("You hear something from the closet do you want to go check it out or run away?")
        if "check it out" in c4:
            print("In the closet you realize that you were hearing voices and they were telling you where your lost dog is and where to find the dog")
        elif "run away and fall through the stairs" in c4:
            print("You run away and the game ends.")
        else:
            print("Stuck thinking.")
    else:
        print("You die")
        c5 = input("You leave the building and go find your dog.")
        if "restart" in c5:
            print("As you walk out the building you hear a dog barking noise in the school and you go back in and see if your dog is in there")
        else:
            print("You listen to the voices and find your dog")