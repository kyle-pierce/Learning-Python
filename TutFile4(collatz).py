# This is a simple program exploring the collatz sequence
# I implemented the sequence using recursion because I 
# figured it would be interesting.  Not sure if this is 
# the 'correct' technique because I have not formally 
# learned recursion in Python.  

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
