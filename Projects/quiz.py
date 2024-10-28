#Beginning
cat_points = 0
dog_points = 0
fish_Points = 0

#Middle
# question 1:
answer = input("On a weekend would you rather A) nap all day, B) go on a hike, or C) Go on a nice walk?")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	fish_Points += 1

# question 2:
answer = input("Are you A) an extrovert, B) an introvert or C) a bit of both?")
if answer == "A":
	dog_points += 1
elif answer == "B":
	cat_points += 1
elif answer == "C":
	fish_Points += 1

# question 3:
answer = input("Would you rather eat lunch A) by yourself, B) with a group or C) with one friend?")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	fish_Points += 1

#question 4
answer = input("do you like, A) halloween B) christmas or C) 4th of july more?")
if answer == "A":
	dog_points += 1
elif answer == "B": 
    cat_points += 1
elif answer == "C":
	fish_Points += 1

#Question 5
answer = input("do you prefer A) sitting B) standing, or C) crouching more?")
if answer == "B":
	dog_points += 1
elif answer == "A":
	cat_points += 1
elif answer == "C":
	fish_Points += 1

#End
if cat_points > dog_points:
	if cat_points > fish_Points:
		print("You are a cat person")
	elif fish_Points > cat_points:
		Print("you are a fish person!")
elif dog_points > cat_points:
	if dog_points > fish_Points:
		print("You are a dog person")
	elif dog_points < fish_Points:
		print("You are a fish person")
else:
	print("you like fish dogs and cats")