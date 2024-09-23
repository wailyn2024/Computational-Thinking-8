while True:
    word = input ("guess? if you dare...")

    if "z" in word:
        print (f"you won! {word}!")
    else:
        print(f"you lost! {word}")

    print ("")