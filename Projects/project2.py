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
else:
    print("You decide to go into the basement")
    c3 = input("The basement hallway goes left to chairs and closet and right to three rooms")
    if "right" in c3 or "three rooms" in c3:
        print("You walk right toward one of the classrooms")
        c4 = input("You hear something from the closet do you want to go check it out or run away?")
        