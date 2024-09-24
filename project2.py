# Intro
print("You walk into the circus.")

print ("the door slams behind you.")
print("")
print("Will you ever be able to escape?")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# choice 1
c1 =input("do you go to the [trampoline] or into the [ring of fire] or the [elephant room]")
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
            print("you put on the hat and a key falls out...")
      else:
            print("you put your hand in the coat pocket and find a key...")

            #choice 4
            print("the key can open up two different rooms which one will you open the [bathroom] or the [kitchen]")
            c4 = input("what room do you open?")
            if "bathroom" in c4:
                  print("you find crazy clowns!")
                  
            else:
                  print("a mob of show monkeys attack you!")
                  
                  #choice 5
                  print("do you [run] or do you try to [attack]?")
                  c5 = input("what will you do?")
                  if "run" in c5: 
                        print("you run and break open the doors escaping from the circus")

                  else: print("you kill all of the monkeys and escape the circus")

                  #choice 6
                  print("now that you have escaped do you [tell people] about what happened or [don't tell]")
                  c6 =  input("what will you say?")
                  if "tell people" in c6: 
                        print("construction comes and breaks the circus down")

                  else: print("nobody will know...")