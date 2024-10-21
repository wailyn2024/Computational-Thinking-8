extrovert_points = 0
introvert_points = 0
middle_points = 0

# Middle: Ask questions
# question 1:
answer = input("At home would you rather A) talk to your neighbor, or B) sleep, or C) call your friend")
if answer == "A":
    extrovert_points += 1
elif answer == "B":
    introvert_points += 1
if answer == "C":
    middle_points += 1

# question 2:
answer = input ("Are you A) going to the grocery store , or B) ordering on amazon? , or C) going to a self serve grocery store")
if answer == "A":
    extrovert_points += 1
elif answer == "B":
    introvert_points += 1
if answer == "C":
    middle_points += 1

# question 3:
answer = input ("Would you rather  A) go to a party, or B) stay at home, or C ) stop by for 5 minutes")
if answer == "A":
    extrovert_points += 1
elif answer == "B":
    introvert_points += 1
if answer == "C":
    middle_points += 1

# question 4
answer = input ("Do you want to  A) go to the picnic, or B) tell everyone your sick, or C ) do a mini picnic with your close friends")
if answer == "A":
    extrovert_points += 1
elif answer == "B":
    introvert_points += 1
if answer == "C":
    middle_points += 1

# question 5
answer = input ("Lets go to school A) present your presentation, or B) just turn it in and dont present, or C ) present it just for your teacher")
if answer == "A":
    extrovert_points += 1
elif answer == "B":
    introvert_points += 1
if answer == "C":
    middle_points += 1

#End: determine results
if extrovert_points > introvert_points and middle_points:
    print("You are a extrovert")
elif introvert_points > extrovert_points and middle_points:
   print("You are a introvert")
if middle_points > introvert_points and extrovert_points:
   print("You are a middle")
elif extrovert_points == introvert_points:
    print("You are in the middle")
if extrovert_points == middle_points:
    print("You are in the a little more on the extrovert side")
elif middle_points == introvert_points:
    print("You are a little on the shy side")
