#Beginning 
summer_points= 0 
fall_points= 0 
#Middle 
answer= input ("Where would you travel to A) California, or B) New York?\n") 
if answer=="A":
    summer_points +=1 
elif answer=="B":
    fall_points+= 1 
answer= input ( "Would you rather A) eat bagels and croissants at a local cafe or B) watch the sunset and have a picnic with friends")
if answer=="A":
    fall_points+=1 
elif answer=="B":
    summer_points+=1  
answer= input ( "Would you rather A) Get a Hydro Flask or B) Get an Owala")
if answer=="A":
    fall_points+=1 
elif answer=="B":
    summer_points+=1  
answer= input ( "Would you rather A) Milk Chocolate or B) Dark Chocolate")
if answer=="A":
    summer_points+=1 
elif answer=="B":
    fall_points+=1
answer= input ( "Would you rather A) Stay in and have a self care night or B) Have a fun and long night with friends")
if answer=="A":
    fall_points+=1
elif answer=="B":
    summer_points+=1 

#End
if summer_points > fall_points: 
    print("You are a summer person")
elif fall_points> summer_points:
    print("You are a fall person")
elif summer_points==fall_points:
    print("You like fall and summer the same")