# Beginning: create variables
cat_points = 0
dog_points = 0
fish_points = 0

# Middle: Ask questions
# question 1:
answer = input("On a weekend would you rather A) nap all day, or B) hike to a lake or C) go shopping?\n")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	fish_points += 1

# question 2:
answer = input("Are you A) an extrovert, or B) an introvert or C) an ambivert?\n")
if answer == "A":
	dog_points += 1
elif answer == "B":
	cat_points += 1
elif answer == "C":
	fish_points += 1

# question 3:
answer = input("Would you rather eat lunch A) by yourself, or B) with a large group or C) a few friends?\n")
if answer == "A":
	cat_points += 1
elif answer == "B":
	fish_points += 1
elif answer == "C":
	dog_points += 1

# question 4:
answer = input("Do you A)laugh out loud, or B) try to keep your laughter to yourself or C) both?\n")
if answer == "A":
	fish_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	cat_points += 1

# question 5:
answer = input("Do you A) call more, or B)text more or C) facetime?\n")
if answer == "A":
	fish_points += 1
elif answer == "B":
	cat_points += 1
elif answer == "C":
	dog_points += 1

# End: determine results
if cat_points > dog_points:
	print("You are a cat person")
elif dog_points > cat_points:
	print("You are a dog person")
elif cat_points == dog_points:
	print("You like cats and dogs the same")
elif cat_points > fish_points:
	print("You are a cat person")
elif fish_points > cat_points:
	print("You are a fish person")
elif cat_points == fish_points:
	print("You like cats and fish the same")
elif dog_points > fish_points:
	print("You are a dog person")
elif fish_points > dog_points:
	print("You are a fish person")
elif dog_points == fish_points:
	print("You like dogs and fish the same")
elif cat_points == dog_points == fish_points:
	print("You like cats, dogs, and fish the same")