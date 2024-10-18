# Beginning: create variables
Cardinal = 0
Puma = 0
Bulldog = 0
 
print ("Just so that you're not biased, I won't tell you the theme of the quiz")
print ("So answer honestly")
c1 = input ("Are you ready?")
if "yes" in c1: 
    print ("lets go!")
else:
	print ("too bad")

# Middle: Ask questions

# question 1:
answer = input("Which color combo do you prefer? A) Red and black, B) green and blue or C) Purple and White ")
if answer == "A" "a":
	Cardinal += 1
elif answer == "B" or "b":
	Puma += 1
elif answer == "C" or "c":
	Bulldog += 1 

# question 2:
answer = input("Which sounds cooler? A) Metro 3A or B) Emerald Sound 1A?")
if answer == "A" "a":
	Cardinal += 1 
	Bulldog += 1
elif answer == "B" or "b":
	Puma += 1


	# question 3:
answer = input("Pick a number. A) 6 or B) 3 ")
if answer == "A" "a":
	Cardinal += 1
elif answer == "B" or "b":
	Puma += 1
	Bulldog += 1 

# question 4:
answer = input("Which is better? A) a school with a football team? or B) one without?")
if answer == "A" "a":
	Puma += 1
	Bulldog += 1
elif answer == "B" or "b":
	Cardinal += 1


	# question 5:
answer = input("Pick one mre number. A) 1,261 , B) 660 or C) 1,642? ")
if answer == "A" "a":
	Cardinal += 1
elif answer == "B" or "b":
	Puma += 1
elif answer == "C" or "c":
	Bulldog += 1 

# end of quiz:
if Cardinal > Puma + Bulldog:
	print("Congrats you're a Cardinal!")
elif Puma > Cardinal + Bulldog :
	print("Oh..you're a puma...sorry..")
elif Bulldog > Puma + Cardinal :
	print("Could be better.... you're a bulldog..") 
