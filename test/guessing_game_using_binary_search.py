low=1
high=1000
guesses=0
print(f'Think of a number between {low} to {high}')
input('Enter to start the game')

guess = 1
while low!=high:
    print(f'Guessing in the range of {low} to {high}')
    guess = low + (high - low) // 2
    high_low = input(f'My guess is {guess}. should I guess higher or lower ?'
                     'Enter h or l, or c if my guess was correct').casefold()
    if high_low =='h':
        low=guess+1
    elif high_low == 'l':
        high=guess-1
    elif high_low == 'c':
        print(f"I got it in {guesses} guesses ")
        break
    guesses = guesses +1
else:
    print(f'You are guessing the {low} number') nf\  dlfnnn