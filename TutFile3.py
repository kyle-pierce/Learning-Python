# This is a fun program which makes you guess numbers
import random

number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        break

if guess == number:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(number))
