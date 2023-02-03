name = input("type your name: ")
print("welcome", name, "to this adventure!")

answer = input("you are on a dirt road, it has come an end and you can go left or right. which way would you like to go? ").lower()

if answer == "left":
    answer = input("you come to a river, you can walk around it or swim accross? (swim/walk) ")
    if answer == "swim":
        print("you swam accross and were eaten by an alligator. ")
    elif answer =="walk":
        print("you walked for many miles, ran out of water, and you lost the game. ")
    else:
        print("not a valid option. you lose ")
elif answer == "right":
    answer = input("you come to a bridge, it looks wobbly. do you want to cross it or head back? (cross/back) ")
    if answer == "back":
        print("you go back and lose. ")
    elif answer =="cross":
        print("you cross the bridge and meet a stranger. do you talk to them? (yes/no) ").lower()

        if answer == "yes":
            print("you talk to the stranger and they give you gold. you win!! ")
        elif answer == "no":
            print("you ignore the stranger and they are offended. you lose :( ")
        else:
            print("not a valid option. you lose.")
    else:
        print("not a valid option. you lose.")
else:
    print("not a valid option. you lose.")

print("thank you for trying", name)
