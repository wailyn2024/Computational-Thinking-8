# Intro
print("You walk into the circus.")

print ("the door slams behind you.")
print("")
print("Will you ever be able to escape?")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# choice 1
c1 =input("do you go to the [trampoline] or into the [ring of fire] or the "elephant room")
if "trampoline"in c1:
      print("you slowly walk to the trampoline")

elif "ring of fire"in c1:
      print("you decide to go to the ring of fire")

      # choice 2
      print("the circus hallway goes left to the changing room and right into the elephant room")
      c2 = input("do you go [left] or [right]?")
      if "left" in c2 or "changing room" in c2:
            print("you walk towards the changing room")
      else:
            print("You walk right towards the bathroom")

      
else:
      print("you decided to go into the elephant room")
      # choice 3
      print("in the changing room you can put on a [coat] or a [hat]")
      c3 = input("what do you put on?")
      if "hat" in c3:
      print("you put on the hat...")
      else:
            print("you put your hand in the coat pocket and find a key...")