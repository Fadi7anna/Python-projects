name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right, which way you want to go? ").lower()

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim accross. Type 'walk' to walk around and 'swim' to swim accross. ")
    if answer == "swim":
        print("You swam accross and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.')


elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
    if answer == "back":
        print("You go back to the main road. Now you can decide to drive to the left. You LOSE")
    elif answer == "cross":
        answer = input(
            "You crossed the bridge and met a stranger. Do you talk to them or not (yes/no)? ")
        if answer == "yes":
            print("You talk to the stranger. He's a serial killer and he kills you. You lose.")
        elif answer == "no":
            print("You ignore the stranger and you win.")

    else:
        print('Not a valid option. You lose.')
    
    print()

else:
    print('Not a valid option. You lose.')
    
print("Thank you for trying,", name)