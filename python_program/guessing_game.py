answer=5
print('Guess the number between 1 to 10')
guess=int(input())

if answer!=guess:
    if guess<answer:
        print('Guess higher number')
    else:
        print('Guess lower number')
    guess=int(input())
    if guess==answer:
        print('You Guess it correctly')
    else:
        print('You didnt guess correctly')
else:
    print("You guess at first")

# if guess<answer:
#     print("Guess higher number")
#     guess=int(input())
#     if guess==answer:
#         print('You guessed it')
#     else:
#         print('You Guesses wrong')
# elif guess>answer:
#     print('guess lower number')
#     guess=int(input())
#     if guess==answer:
#         print('Wel done you guessed it')
#     else:
#         print('You Guessed Wrong')
# else:
#     print("You guess correct number at first chance")