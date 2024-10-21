#setup
drummer_points =0
guitarist_points = 0
bassist_points = 0

print("this Quiz will figure out what instrument you should play/play")

#Questions

#Question 1:
answer = input("On a weekend would you rather A) nap all day, or B) go on a hike?")
if answer.lower() == "A":
	drummer_points += 2
	bassist_points += 1
elif answer.lower() == "B":
	guitarist_points += 1

# question 2:
answer = input("Are you A) an extrovert, or B) an introvert?")
if answer.lower() == "A":
	guitarist_points += 2
	bassist_points += 1
elif answer.lower() == "B":
	drummer_points+= 1
	bassist_points +=1

# question 3:
answer = input("how much do you practice before a performance A) not at all B) 9 hours  C) 16 hours ")
if answer.lower() == "A":
	drummer_points += 5
elif answer.lower() == "B":
	bassist_points += 2
else:
	guitarist_points += 2

answer = input("what do you think of other instruments, A) they're all boring and I don't care B) I enjoy them and think they help make music interesting C) whatever, they're chill")
if answer.lower() == "A":
	guitarist_points += 5
elif answer.lower() == "C":
	drummer_points += 1
else: 
	bassist_points += 5
	
answer = input("how good are you at your instrument A) amazing, probably the best B)I'm alright just trying my best C) I didn't even know I played an instrument")
if answer.lower() == "A":
	guitarist_points += 1
elif answer.lower() == "B":
	bassist_points += 1
else:
	drummer_points +=1

answer = input("what kind of impression do you leave on others A) none at all most people forget me B) people usually think of me as confident and outgoing C) people usually think of me as calm and laid back")
if answer.lower() == "A":
	bassist_points += 1
elif answer.lower() == "B":
	guitarist_points += 1
elif answer == "C":
	drummer_points += 1
#results
if drummer_points >= guitarist_points:
	print ("you are drummer")
elif guitarist_points >= drummer_points:
	print("you are a guitarist")
else:
	print("you are a bassist")
print("this quiz was targeted to musicians and also very biased")
