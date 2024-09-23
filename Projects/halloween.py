#intro
print("its halloween night and you're ready to go home but you see a haunted house and decide to check it out with a couple of your friends.")
print("-----------------------------------------")
print("you walk in and see a bunch of bats fly past you screeching as the door creaks to a close behind you.")
print("------")
print("will you escape?")
#choice 1
c1 = input("do you choose to go up the [stairs] or into the [basement] or you can split up with your friends and [go alone] down a creepy hallway that seems to be calling your name?")
if "stairs" in c1:
    print("you slowly walk up the creaky stairs.")
    #choice 2
    print("the upstairs leads to a narrow hallway with 2 rooms, an [office] and a [bedroom]")
    c2 = input("do you want to go into the [bedroom] or the [office]?")
    if "bedroom" in c2:
        print("you go into the bedroom")
        #choice 3
        print("you see the bed and a closet full of clothes that seems to be hiding something")
        c3 = input("do you want to investigate the [bed] or the [closet]?")
        if "bed" in c3:
            print("you investigate the bed and it turns out there is a slide under the bed and it brings you a secret room that has a 3 digit code door")
            print("see 2 numbers on the wall the first, 123, and the second, 321")
        #choice 6
        c4 = input("do you choose to put in, [123], or [321]")
        if "123" in c4:
            print("you put in 123")
            print("it doesnt work and the slide closes behind you and you get trapped and die of thirst")
        else:
            print("you put in 321 and it works!")
            print("the door slowly creaks open")
            print("you escape out the door and run home")
            print("you win!")
            #choice 7
    else:
        print("you enter the office")
        print("you enter the office")
        print("you die")
elif "basement" in c1:
    print("you decide to go down into the basement.")
    #choice 4
    print("when you get down into the basement to your left you see an oddly big bookshelf, and to your right a bathroom")
    c3 = input("do you choose to investigate the [bookshelf] or the [bathroom?]")
    if "bookshelf" in c3 or "left" in c3:
        print("you investigate the bookshelf to find the its a secret room!")
        #choice 5
        print("in the secret room you find a 3 digit code door and 2 numbers on the wall, 123, and 321")
        c4 = input("do you choose to put in, [123], or [321]")
        if "123" in c4:
            print("you put in 123")
            print("it doesnt work and the bookshelf closes behind you and you get trapped and die of thirst")
        else:
            print("you put in 321 and it works!")
            print("the door slowly creaks open")
            print("you escape out the door and run home")
            print("you win!")


    else:
        print("you decide to go investigate the bathroom")

else:   
    print("strange choice? but you split up with your friend and go down the creepy hallway.")
    print("as soon as you start walking down you see a clown and start sprinting as fast as you can and get chased into a trap and die")
    print("you loose=(")