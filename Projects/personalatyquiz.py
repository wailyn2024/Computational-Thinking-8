cat_points = 0
dog_points = 0
fish_points = 0 

# question 1:
answer = input("On a weekend would you rather A) nap all day, B) go on a hike, C) read a book? ")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	fish_points += 1

# question 2:
answer = input("Are you A) an extrovert, B) an introvert, C) neutral? ")
if answer == "A":
	dog_points += 1
elif answer == "B":
	cat_points += 1
elif answer == "C":
	fish_points += 1

# question 3:
answer = input("Would you rather eat lunch A) by yourself, or B) with a group, C) with one friend ")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	fish_points += 1

# question 4;
answer = input("Do you prefer A) breakfast, B) lunch, C) or dinner? ")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	fish_points += 1
# end of quiz:
if cat_points > fish_points and cat_points > dog_points:
	print("You are a cat person")
elif dog_points > fish_points and dog_points > cat_points:
	print("You are a dog person")
if fish_points > cat_points and fish_points > dog_points:
	print("you are a fish person")