from random import randint

def get_dice():
    return randint(1,6)

while True:
    print("Eyes: " + str(get_dice()))
    answer = input("Do you want to roll the dices again?(y/n)")
    if answer != "y":
        break


    
