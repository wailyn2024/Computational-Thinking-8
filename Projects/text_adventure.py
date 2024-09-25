# Intro
print("")
print ("You have landed in Barbie land!!!!!")
print("you have a chance to meet either Barbie or Raquelle")
print("if you become friends Barbie you will help run barbie land")
print("buttt in you become friends with Raquelle you will become rich")
print ("")

#choice oneee
C1= input("do you choose to go to [Barbie] or [Raquelle]")
if "Barbie" in C1:
    print("")
    print("You have arrived at city hall! standing to meet you is your new friend Barbie")
   #choice twoo abt barbiee
    print ("Barbie has two options to give you abt city hall!")
    C2= input("you can either be [governor] or [a court justice]")
    if "governor" in C2:
        print ("umm ok sounds good ill set up your office")
    else:
        print ("yayyyy okk ill set up your office next to mine since im governor!!")

else:
    print("")
    print("You have been teleported to Raquelles bat cave, walk in and find her in the Vector W2")
    # choice three abt Raquelle
    print("Raquelle need to know you level of hate for Barbie")
    C3= input (" Raquelle wants to know if you [hate] or [are ok with] Barbie")
    if "hate" in C3:
        print("")
        print ("AMAZING!!! you can be my bestie and brain stormer!")
    else:
        print("")
        print ("oh.... umm.. ok ig we can be friends you can be my cleaner...")

print("")
C4= input ("do you want to go out and [explore the town], [stay where you are], or [try to make more friends]?")
if "explore the town" in C4:
    print ("omg suchh a good choice there is so many shops in the townn!!")
elif "stay where you are" in C4:
    print ("ok loyal workerrrrr, i see youuu")
else:
    print("lolz the more friends the marrier!")

C5= input ("its time for bed you have worked hard all day do you want to continue your live at barbie land?")
if "yes" in C5:
    print ("congrats! im so glad you chose to stay!")
else:
    print ("so sad to see you go had so much time with you though")


