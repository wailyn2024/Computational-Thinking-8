from turtle import onkey


cat_points = 0
dog_points = 0
monkey_points = 0

#Beginning
# question 1:
answer = input("On a weekend would you rather A) nap all day, or B) go on a hike? or C) climb a tree")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	monkey_points += 1

# question 2:
answer = input("Are you A) an extrovert, or B) an introvert? or C) an ambivert")
if answer == "A":
	dog_points += 1
elif answer == "B":
	cat_points += 1
elif answer == "C":
	monkey_points += 1

#Middle
# question 3:
answer = input("Would you rather eat lunch A) by yourself, or B) with a group? or c) eat lunch in a tree")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	monkey_points += 1
	
# question 4:
answer = input("would you rather sleep A) by yourself, or B) with a group or C) sleep in a tree")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	monkey_points += 1

# question 5:
answer = input("are you a cat a dog or a monkey person A) cat, or B) dog, or C) monkey")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	monkey_points

#end
# end of quiz:
if cat_points > dog_points and cat_points > monkey_points:
	print("You are a cat person")
elif dog_points > cat_points and dog_points > monkey_points:
	print("You are a dog person")
elif monkey_points > dog_points and monkey_points > cat_points:
	print("you are a monkey person")