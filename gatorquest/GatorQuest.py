name = input("Hero name: ")
choice = input ("Go left or right?: ")

sword = False 

if choice == "left":
    print("You spot a chest in a nearby bush")
    chest = input("Open it?: ")
    if chest == "yes":
        print("You found a sword!")
        sword = True
    elif chest == "no":
        print("You walk away, maybe it contained a trap.")
    else:
        print("You must choose yes or no.")
elif choice == "right":
    print("A shadowy figure appears in front of you")
    fight = input("Fight or flee?")
    if fight == "fight":
        if sword:
            print("You pull out your sword and get in a fighting stance.")
elif choice == "forward":
    print("You walk into a wall, hitting your head.")
elif choice == "backward":
    print("You hesitate. You're here for a reason, you can't go back now.")
else:
    print("You must choose a direction.")