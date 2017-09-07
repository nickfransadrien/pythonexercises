from random import randint

random_number = randint(1,100)
while True:
    try:
        number = int(input("Make a guess: "))
    except:
        print("You have to type a number")
        continue
    if number == random_number:
        print("You Guessed it")
        break
    if number < random_number:
        print("Too low")
    if number > random_number:
        print("Too high")
