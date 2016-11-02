# This is a simple program exploring the collatz sequence

def collatz(number):
    print(str(int(number)))
    if (number != 1):
        if (number % 2 == 0):
            collatz(number / 2)
        else:
            collatz((number * 3) + 1)

print('Please enter an integer: ', end = '')
try:
    number = int(input());
    print()
    collatz(number)
except ValueError:
    print('Invalid Input')
