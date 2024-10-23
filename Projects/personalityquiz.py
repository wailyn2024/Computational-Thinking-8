	#Beginning setup
Jean_points = 0
Furina_points = 0
Mona_points = 0
print("Which Genshin character are you")
# question 1:
answer = input("On a weekend would you rather A) learn a new skill, B) go to the theatre, or C) take a break from work and just relax?")
if answer.upper() == "A":
	Mona_points += 1
elif answer.upper() == "B":
	Jean_points += 1
elif answer.upper() == "C":
	Furina_points += 1

#MIDDLE: QUESTIONS
print("     ")
answer = input("Are you an A) introvert, B) extrovert, or C) ambivert?")
if answer.upper() == "A":
	Mona_points += 1
if answer.upper() == "B":
	Jean_points += 1
	Furina_points += 1
elif answer.upper() == "C":
	Furina_points += 2

print("     ")

print("Shoot, running out of money. Is your response:")
answer = input("A), Oh, I have a new job coming up. It'll be fine, B) What?? That's impossible, I had a budget! or C) I don't have any time to run any odd jobs, my schedule is already packed, or D) This isn't new to me... ")
if answer.upper() == "A":
	Jean_points += 1
elif answer.upper() == "B":
	Furina_points += 1
	Mona_points += 1
elif answer.upper() == "C":
	Jean_points += 1
elif answer.upper() == "D":
	Mona_points += 1

print("     ")
answer = input("Would you rather eat A) desserts, B) salad, or C) pizza?")
if answer.upper() == "A":
	Furina_points += 1
elif answer.upper() == "B":
	Mona_points += 1
elif answer.upper() == "C":
	Jean_points += 1


	print("     ")
print("You are crying. Why?")
print("A) People keep asking me for things and I can't handle all these requests anymore.")
print("B) Everythings feeling really overwhelming and I can't keep up.")
answer = input("C) I feel like I've been faking everything and it's getting to be too much.")
if answer.upper() == "A":
	Jean_points += 1
elif answer.upper() == "B":
	Mona_points += 1
elif answer.upper() == "C":
	Furina_points += 1
	print("     ")
print("How do you think others view you?")
print("A) I am perfect and always positive, putting on a show and making others laugh.")
answer = input("B) I'm a hard worker who is always ready to give a hand to assist others.")
if answer.upper() == "A":
	Jean_points += 1
elif answer.upper() == "B":
	Furina_points += 1
	Mona_points += 1

answer = input("What's your favorite time of day? A) Morning, B) Afternoon, or C) Evening?")
if answer.upper() == "A":
	Jean_points += 1
elif answer.upper() == "B":
	Mona_points += 1
elif answer.upper() == "C":
	Furina_points += 1

answer = input("A) Gold or B) Silver")
if answer.upper() == "A":
	Jean_points += 1
	Furina_points += 1
elif answer.upper() == "B":
	Mona_points += 1

answer = input("A) Stars, B) Moon, or C) Sun?")
if answer.upper() == "A":
	Mona_points += 1
elif answer.upper() == "B":
	Furina_points += 1
elif answer.upper() == "C":
	Jean_points += 1

# end of quiz:
#Results
if Furina_points > Jean_points and Furina_points > Mona_points:
	print("You are Furina, the actress and former god.")
	print("Please for the love of god go get a hug. Or don't. Either way, it's pretty concerning that you're always acting.")
	print("When you talk to others, you have a 50/50 chance of either being very bubbly or quiet and shy.")
elif Jean_points > Furina_points and Jean_points > Mona_points:
	print("You are Jean, the leader of Mondstat.")
	print("Look, letting people step all over you is not a good thing even if you get praise for completing jobs for them.")
	print("In the end, you have to take a step back and take a break for you.")
elif Mona_points > Furina_points and Mona_points > Jean_points:
	print("You are Mona, the Astrologist.")
	print("Though you are broke, you're trying your best- which is what really matters.")
	print("Just...stop spending money on things you don't need.")