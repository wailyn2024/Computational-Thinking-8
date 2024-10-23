#Beginning
cat_points = 0
dog_points = 0 
neither_points = 0 
#Middle
# question 1:
answer = input("On a weekend would you rather A) nap all day, or B) go on a hike? C) Neither")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	neither_points += 1

# question 2:
answer = input("Are you A) an extrovert, or B) an introvert? C) Neither")
if answer == "A":
	dog_points += 1
elif answer == "B":
	cat_points += 1
elif answer == "C":
	neither_points += 1
# question 3:
answer = input("Would you rather eat lunch A) by yourself, or B) with a group? C) Neither")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	neither_points += 1
# question 4:
answer = input("Would you rather play basketball professionally A) by yourself, or B) with a group? C) Neither")
if answer == "B":
	cat_points += 1
elif answer == "A":
	dog_points += 1
elif answer == "C":
	neither_points += 1
# question 5: 
answer = input("Would you rather code A) by yourself, or B) with a group? C) Neither")	
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	neither_points += 1
# End
if cat_points > dog_points:
	print("You are a cat person")
elif dog_points > cat_points:
	print("You are a dog person")
elif cat_points == dog_points:
	print("You like cats and dogs the same")