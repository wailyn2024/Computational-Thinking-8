#intro

print("You wake up in a cobbled room")
print("The room is covered in dust and cobwebs it looks like it hasn't been used in a while")
print("their are metal bars preventing your escape.")
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
        if "bed" in e1 or "sleep" in e1:
            print("you wake up to see that your cell door is unlocked and the key to the jukebox on the floor")
            e2 = input("do you explore the now open [hallway] or mess with the [jukebox]")
            if "hallway" or "run" is e2:
                print("You are exploring the hallway when a man in wearing a black ski mask starts chasing you")
                print("You run away from him")
                #True Ending
                d1 = input("Do you [run] and try to shake him off or [fight]")
                if "run" in d1 or "hallway" in d1:
                    print("He follows you but you manage to shake him off")
                    print("You find your self in a room full of men in black ski masks")
                    print("they are praying to your figure")
                    print("they all turn towards you.")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("You find yourself strapped to a chair they each take turns repeatedly stabbing you")
                    print("YOUR DEAD or ARE YOU?")
                    r1 = input("_________________________________________________")
                    print("You find yourself wearing a black mask")
                    print("You are carrying the body of you?")
                    print("ALL PATHS LEAD TO DEATH")
                else:
                    print("He lunges at you you try to defend yourself.")
                    print("He stabs you with a butter knife.")
                    print("YOUR DEAD")
            elif "Jukebox" or "key" in e2:
                print ("You insert the key into they jukebox")
                print ("You find a small butter knife")
                print ("A man in wearing a black ski mask passes your cell")
                c3 = input("Do you [hide] or [stay]")
                if "stay" in c3:
                    print("The man in the ski mask attacks you")
                    print("You try to defend yourself with you newly acquired butter knife")
                    print("He punches you")
                    print("He picks up your knife")
                    print("He hovers over you and repeatedly stabs you")
                    print("your dead")
                else:
                    print("You hide behind the jukebox")
                    print("He doesn't find you")
                    print("He leaves")
                    c4 = input("Do you continue [hiding] or[Run]")
                    if "Run" in c4:
                        print("He catches you")
                        print("YOUR DEAD")
                    else:
                        print("He catches you")
                        print("YOUR DEAD")
            else:
                print("You go back to sleep")
                print("You never wake back up")
                print("YOUR DEAD")
            #BLACK SKI MASK remember to add
        else:
            print("A man in wearing a black ski mask comes in your cell")
            print("He has a butter knife")
            print("You try to fight back")
            print("YOUR DEAD")
    #Ending 2
    else:
        End = input("A man in wearing a black ski mask comes in your cell")
        print("He has a butter knife")
        print("You try to fight back")
        print("YOUR DEAD")
else:
    print("you go back to sleep")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("you wake up in your bed when suddenly a bag is placed up on your head")
    #Ending 1
    End = input("you find yourself in a cross shaped coffin. You scream for help but no one comes for you.")
    print("YOU HAVE DIED")
    