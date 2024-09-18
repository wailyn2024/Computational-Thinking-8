print("guess what grandma's rule is.")
print("grandma likes eight and doesn't like four")

while True:
    word = input("What do you think grandma likes?")

    if len(word) > 10:
        print("grandma dislikes (word).")
    elif len(word) < 5:
        print("grandma dislikes (word).")
    else:
        print("grandma likes (word).")
print(" ")
