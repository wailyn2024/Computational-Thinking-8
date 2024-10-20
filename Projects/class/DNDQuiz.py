# Variables
largest = {
    "barbarianpoints": 0,
    "bardpoints": 0,
    "clericpoints": 0,
    "druidpoints": 0,
    "fighterpoints": 0,
    "monkpoints": 0,
    "paladinpoints": 0,
    "rangerpoints": 0,
    "rougepoints": 0,
    "sorcererpoints": 0,
    "warlockpoints": 0,
    "wizardpoints": 0,
    "artificerpoints": 0,
}

# Question 1
print("Are you studious or do you go with the flow or both?")
answer = input("").lower()
if "flow" in answer:
    largest["barbarianpoints"] += 1
    largest["bardpoints"] += 1
    largest["rangerpoints"] += 1
    largest["fighterpoints"] += 1
    largest["sorcererpoints"] += 1
if "studious" in answer:
    largest["wizardpoints"] += 1
    largest["clericpoints"] += 1
    largest["warlockpoints"] += 1
    largest["artificerpoints"] += 1
if "both" in answer:
    largest["bardpoints"] += 1
    largest["rougepoints"] += 1
    largest["paladinpoints"] += 1

# Question 2
print("You come up to a locked door, do you:")
print(" A: Use magic to open it")
print(" B: Force it open")
print(" C: Try to pick a lock")
answer = input("").upper()
if answer == "A":
    largest["wizardpoints"] += 1
    largest["sorcererpoints"] += 1
    largest["warlockpoints"] += 1
    largest["paladinpoints"] += 1
    largest["druidpoints"] += 1
elif answer == "B":
    largest["fighterpoints"] += 1
    largest["barbarianpoints"] += 1
    largest["rangerpoints"] += 1
    largest["artificerpoints"] += 1
elif answer == "C":
    largest["bardpoints"] += 1
    largest["rougepoints"] += 1
    largest["monkpoints"] += 1
    largest["clericpoints"] += 1

# Question 3
print("Rate how angry of a person you are! (0-10)")
answer = input("")
if answer == "0":
    largest["monkpoints"] += 1
    largest["clericpoints"] += 1
elif answer == "1":
    largest["paladinpoints"] += 1
elif answer == "2":
    largest["druidpoints"] += 1
elif answer == "3":
    largest["rangerpoints"] += 1
elif answer == "4":
    largest["bardpoints"] += 1
    largest["wizardpoints"] += 1
elif answer == "5":
    largest["artificerpoints"] += 1
elif answer == "6":
    largest["sorcererpoints"] += 1
elif answer == "7":
    largest["warlockpoints"] += 1
elif answer == "8":
    largest["rougepoints"] += 1
elif answer == "9":
    largest["fighterpoints"] += 1
elif answer == "10":
    largest["barbarianpoints"] += 1
#question 4
print("in the party are you")
print("The leader")
print("The smart one")
print("The healer")
print("The funny one")
answer = input("")
if "leader" in answer:
    largest["fighterpoints"] += 1
    largest["barbarianpoints"] += 1
    largest["paladinpoints"] += 1
elif "smart" in answer:
    largest["artificerpoints"] += 1
    largest["wizardpoints"] += 1
    largest["rougepoints"] += 1
    largest["monkpoints"] += 1
elif "healer" in answer:
    largest["clericpoints"] += 1
    largest["druidpoints"] += 1
    largest["rangerpoints"] += 1
elif "funny" in answer:
    largest["sorcererpoints"] += 1
    largest["warlockpoints"] += 1
    largest["bardpoints"] += 1
#Question 5
print("Melee or magic")
answer = input("")
if "magic" in answer:
    largest["wizardpoints"] += 1
    largest["druidpoints"] += 1
    largest["clericpoints"] += 1
    largest["sorcererpoints"] += 1
    largest["warlockpoints"] += 1
    largest["bardpoints"] += 1
if "melee" in answer:
    largest["barbarianpoints"] += 1
    largest["roguepoints"] += 1
    largest["rangerpoints"] += 1
    largest["fighterpoints"] += 1
    largest["monkpoints"] += 1
    largest["paladinpoints"] += 1
# find most points
mostpoints = max(largest, key=largest.get)
print("Your highest score for a class is: " + mostpoints)
