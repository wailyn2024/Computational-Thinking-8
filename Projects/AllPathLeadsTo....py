#intro
print("You wake up in a cobbled room")
print("The room is covered in dust and cobwebs it looks like it hasn't been used in a while")
print("their are metal bars covering your escape.")
print("You see a old juke box and a mattress")
#choice 1
c1 = input("what do you do?. Do you investigate the [jukebox] or sleep on the [bed]?")
if "jukebox" in c1:
    print("you find a little hole it looks big enough to hold a key")
    #right choice 2
    c2 = input("You could either investigate the [bed] or [wait] for help")
    if "bed" in c2:
        print("you find nothing under the bed")
        #right choice 2
        e1 = input("do you go back to [sleep] or [wait]")
        if "bed" or "sleep" in e1:
            print("you wake up to see that your cell door is unlocked and the key to the jukebox on the floor")
            e2 = input("do you explore the now now open [hallway] or mess with the [jukebox]")
            #BLACK SKI MASK remember to add
        else:
            print("A man in wearing a black ski mask comes in your cell")
            print("He has a knife")
            print("You try to fight back")
            print("YOUR DEAD")
    #Ending 2
    else:
        print("A man in wearing a black ski mask comes in your cell")
        print("He has a knife")
        print("You try to fight back")
        print("YOUR DEAD")
else:
    print("you go back to sleep")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("you wake up in your bed when suddenly a bag is placed up on your head")
    #Ending 1
    print("you find yourself in a cross shaped coffin. You scream for help but no one comes for you.")
    print("YOU HAVE DIED")
 