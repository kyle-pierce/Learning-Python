#plays Tic-Tac-Toe with you (Jonah?) but it doesn't know when we're done (yet)

theBoard = {'t-L': ' ', 't-M': ' ', 't-R': ' ',
            'm-L': ' ', 'm-M': ' ', 'm-R': ' ',
            'b-L': ' ', 'b-M': ' ', 'b-R': ' '}

def printBoard(board):
    print(board['t-L'] + '|' + board['t-M'] + '|' + board['t-R'])
    print('-+-+-')
    print(board['m-L'] + '|' + board['m-M'] + '|' + board['m-R'])
    print('-+-+-')
    print(board['b-L'] + '|' + board['b-M'] + '|' + board['b-R'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'
        
