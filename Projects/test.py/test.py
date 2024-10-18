pg = 0
center = 0
print("")

# Question 1
answer = input("Would you say you're big and fat and strong (A), or tiny, weak, and shifty (B)? ")
if answer == "A" or answer in ["big", "fat", "strong"]:
   center += 1
   print("")
elif answer == "B" or answer in ["tiny", "weak", "shifty"]:
   pg += 1
   print("")

# Question 2
answer = input("Would you rather get blocks (A), or get steals (B)? ")
if answer == "A" or answer == "blocks":
   center += 1
   print("")
elif answer == "B" or answer == "steals":
   pg += 1
   print("")

# Question 3
answer = input("Game winning dunk (A), or game winning shot (B)? ")
if answer == "A" or answer == "dunk":
   center += 1
   print("")
elif answer == "B" or answer == "shot":
   pg += 1
   print("")

answer = input("Would you prefer to play in the paint (A), or on the perimeter (B)? ")
if answer == "A" or answer in ["paint"]:
    center += 1
    print("")
elif answer == "B" or answer in ["perimeter"]:
    pg += 1
    print("")

# Question 5
answer = input("Do you enjoy setting screens (A), or running fast breaks (B)? ")
if answer == "A" or answer in ["screens"]:
    center += 1
    print("")
elif answer == "B" or answer in ["fast breaks"]:
    pg += 1
    print("")

# End of quiz
if pg > center:
    print("You are a pure point guard.")
elif center > pg:
    print("You are a dominant center.")
else:
    print("You have a balanced style.")