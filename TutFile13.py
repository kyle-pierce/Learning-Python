#! python3
# TutFile13.py - takes a list of lists and prints it in a nice looking table

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def getMaxLength(col):
    maxLength = 0;
    for i in range(len(tableData[col])):
        if (len(tableData[col][i]) > maxLength):
            maxLength = len(tableData[col][i])
    return (maxLength + 1)

for i in range(len(tableData[0])):
    print(tableData[0][i].rjust(getMaxLength(0)), end='')
    print(tableData[1][i].rjust(getMaxLength(1)), end='')
    print(tableData[2][i].rjust(getMaxLength(2)))

