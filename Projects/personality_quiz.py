#setup
cat_points = 0
dog_points = 0
crow_points = 0


animal_points = [cat_points,dog_points,crow_points]

#middle
# question 1:
answer = input("On a weekend would you rather A) nap all day, B) go on a hike, or C) make a piece of art? ")
if answer.lower() == "a":
	cat_points += 1
elif answer.lower() == "b":
	dog_points += 1
elif answer.lower() == "c":
	crow_points += 1

# question 2:
answer = input("Are you A) an extrovert, B) an introvert, or C) an ambivert? ")
if answer.lower() == "a":
	dog_points += 1
elif answer.lower() == "b":
	cat_points += 1
elif answer.lower() == "c":
	crow_points += 1

# question 3:
answer = input("Would you rather eat lunch A) by yourself, B) with a large group, or C) with a small group? ")
if answer.lower() == "a":
	cat_points += 1
elif answer.lower() == "b":
	dog_points += 1
elif answer.lower() == "c":
	crow_points += 1

#question 4:
answer = input("would you rather A) live by yourself, B) with your friends, C) with you family? ")
if answer.lower() == "a":
	cat_points += 1
elif answer.lower() == "b":
	dog_points += 1
elif answer.lower() == "c":
	crow_points += 1
#question 5:
answer = input("do you like A) tea, B) coffee, C) water? ")
if answer.lower() == "a":
	cat_points += 1
elif answer.lower() == "b":
	dog_points += 1
elif answer.lower() == "c":
	crow_points += 1
#ending
animal_points = [cat_points,dog_points,crow_points]
list_max = max(animal_points)
print(list_max)

if list_max == dog_points and list_max == cat_points:
	print("you are a mix of dog and cat people")
elif list_max == crow_points and list_max == dog_points:
	print("you are a mix of crow and dog people")
elif list_max == crow_points and list_max == cat_points:
	print("you are a mix of crow and cat people")
elif list_max == cat_points:
	print("you are a cat person")
elif list_max == dog_points:
	print("you are a dog person")
elif list_max == crow_points:
	print("you are a crow person")



