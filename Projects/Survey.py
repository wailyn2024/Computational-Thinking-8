#Setup
value=["1","2","3"]
spam =[5,-5]
points = 0
print("would you rather. A). B)")
choice = input()
choice = choice.lower()
#QUESTIONS
match choice:
    case "a":
        print(f"{value[0]}")
        points +=1
    case "b":
        print(f"{value[2]}")
        points -=1
print("A or B")
choice2 = input()
choice = choice2.lower()
match choice:
    case "a":
        print(f"{value[0]}")
        points+=1
    case "b":
        print(f"{value[2]}")
        points-=1
print("A or B")
choice2 = input()
choice = choice2.lower()
match choice:
    case "a":
        print(f"{value[0]}")
        points+=1
    case "b":
        print(f"{value[2]}")
        points-=1
print("A or B")
choice2 = input()
choice = choice2.lower()
match choice:
    case "a":
        value = value[0]
        print(value)
        points+=1
    case "b":
        value = value[2]
        print(value)
        points-=1
print("A or B")
choice2 = input()
choice = choice2.lower()
match choice:
    case "a":
        print(f"{value[0]}")
        points+=1
    case "b":
        print(f"{value[2]}")
        points-=1
#END
if points==spam:
    print("SPAM ERROR")
else:
    if points >0:
        print("W")
    elif points<0:
        print("L")
    else:
       print("N")