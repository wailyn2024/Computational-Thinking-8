#intro 
print ("you and your friend go to a spooky maze")
print (" you went to find a tressure, but you get lost on the way")
print ("")
print ("will you be able to get out?")

#choice 1
c1 = input("Do you choose to go [with your friend] or [split up?]")
if "split up" in c1:
    print ("you wave to your friend and go your own way.")
    print("you are now split up from your friend and are walking though the maze")
else:
    print("you stay together")
 #choice 2
c2 = input("do you go [left] or [right]?")
if "right" in c2:
        print ("you turn right but you hear something going your way")
else:
     print ("you turn left and look back but your friend is missing?")
    #choice 3
     print ("you have to pick either [run] and leave your friend behind or [go look for them]")
c3 = input ("what will you pick?")
if "run" in c3:
     print ("you run turning left and right in the maze until you find a big golden box")
elif "go look for them" in c3:
     print ("you turn around and run around the maze looking for them")
else: