import random

answer= random.randint(1,10)# this function will generate the random number between 1 to 10
print(answer)
guessed=0
print('Guess the number between 1 to 10')

while guessed!=answer:
    guessed = int(input())

    if answer==guessed:
        print("You guessed the number")
    else:
        if guessed<answer:
            print('Guess higher number')
        else:
            print('Guess lower number')
