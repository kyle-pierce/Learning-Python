#this is for storing the names of cats

catNames = []
name = 'starterName'

while (name != ''):
    print('What is the name of your cat?')
    name = input()
    catNames = catNames + [name]    #list concatenation

print('The cat names are: ')
for name in catNames:   #for-each loop
    print(' ' + name)
