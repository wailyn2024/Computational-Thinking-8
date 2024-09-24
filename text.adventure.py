#Intro
print("You walk into the dark quiet green forrest that your cat ran into, you get a shiver down your spine.")
print("You see a small house...")
print("A little girl peaks out at you from one of the windows")
print("Will ever you find your cat?")

#choice 1
c1 = input("Do you [knock] on the door and talk to the little girl or do you run away from the house and keep looking for your cat [elsewhere]?")
if "knock" in c1:
    print("You cautiously up to the door and knock 4 times")
    c2 = input("The little girl opens the door and asks what you want. Up close you can see her skin is very pale, and she is holding a needle and pouch. Do you ask her if she has seen your [cat] anywhere, or do you [ask] her about the needle and pouch?")
    if "cat" in c2:
        print("She says she hasn't seen any cats, but insists you come inside.")
        # choice 4
        c4 = input("You walk inside and she gives you some tea. She tells you about how there was a curse put on the forrest, and if you want to survive you should drink her tea and get out as soon as possible. You remind her that you only came for you cat and you want to find her, but she insists its not worth it. Do you [listen] to the little girl and get out, leave the house but [continue looking] for you cat, or do you tell her shes crazy and demand to know about the needle and pouch? ")
        if "listen" in c4:
            print("You escape and are safe, but cat-less.")
            print("You win!!")
        elif ""
    else:
        print("She quickly hides the needle and pouch behind her back and looks at you, disturbed. She tells you to come inside, and you decide to follow her request.")
        
else:
    print("You hurry away from the creepy little house to a murky pond in the forrest")
    print("You hear faint whispers all around you and suddenly feel like there are a million eyes watching you. The thought of finding your cat leaves your mind completely.")
    c3 = input("Do you [yell] asking who the whispers belong to or do you [get in] the water?")
    if "yell" in c3:
        print("The whispers increase in speed and volume. You cant even make out what they are saying, but you start to feel a cold tightness around you neck. You gasp for air as you fall into the pond, never to be seen again.")
        print("You lose haha why would you yell?!")
    else:
        print("As soon as you step foot into the water, your sense hearing completely fades. You start to see sad children's heads peeking out the water around you, all staring at you. As your sense of hearing starts to fade back, all you could hear was their cries.")
        print ("You lose sorry")







