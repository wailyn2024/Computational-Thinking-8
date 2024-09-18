# choice 1 
c1 = input("Do you go up the [park] or into the [movies]")
if "park" in c1:
    print("You go to the park")

    # choice 2 
    print("The park has a swing to the left and a slide to the right.")
    c2 = input("Do you go [left] or [right]?")
    if "left" in c2 or "swing" in c2:
        print("You walk left towards the swing.")
    # choice 3 
    print("The swings are full but there is an ice cream shop and a cafe")
    c3 = input("Do you go [left] or [right]?")

    else:
        print("You walk right towards the slide.")


else:
    print("You decide to go into the movies")