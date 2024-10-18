#beginning of quiz
winter_points = 0
summer_points = 0
spring_points = 0
fall_points = 0


# middle of quiz:
answer = input("Would you rather A) go to the beach, B) play in the snow, C) pick pumpkins, or D) go for a hike?")
if answer == "A" or "a":
	summer_points += 1
elif answer == "B" or "b":
	winter_points += 1
elif answer == "C" or "c":
	fall_points += 1
elif answer == "D" or "d":
	spring_points += 1
answer = input("would you rather go A) sledding, B) surfing, C) walking, or D) biking?")
if answer == "A" or "a":
	winter_points += 1
elif answer == "B" or "b":
	summer_points += 1
elif answer == "C" or "c":
	fall_points += 1
elif answer == "D" or "d":
	spring_points += 1


answer = input("Would you celebrate A) hanukah/Christmas, B) 4th of July, C) Halloween, D) Easter/Passover?")
if answer == "A" or "a":
	winter_points += 1
elif answer == "B" or "b":
	summer_points += 1
elif answer == "C" or "c":
	fall_points += 1
elif answer == "D" or "d":
	spring_points += 1

answer = input("Would you rather drink A) hot chocolate, B) lemonade, C) apple cider, D) Shirley Temple")
if answer == "A" or "a":
	winter_points += 1
elif answer == "B" or "b":
	summer_points += 1
elif answer == "C" or "c":
	fall_points += 1
elif answer == "D" or "d":
	spring_points += 1

answer = input("Would you rather eat A) soup, B) watermelon, C) turkey, D) burgers?")
if answer == "A" or "a":
	winter_points += 1
elif answer == "B" or "b":
	summer_points += 1
elif answer == "C" or "c":
	fall_points += 1
elif answer == "D" or "d":
	spring_points += 1
	
#end of quiz

if summer_points > winter_points and summer_points > fall_points and summer_points > spring_points:
	print("You are a summer person!")
if winter_points > fall_points and winter_points > spring_points and winter_points > summer_points:
	print("You are a winter person!")
if fall_points > winter_points and fall_points > summer_points and fall_points > spring_points:
	print("You are a fall person!")
if spring_points > winter_points and spring_points > fall_points and spring_points > summer_points:
	print("You are a spring person!")

