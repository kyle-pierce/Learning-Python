#Comma-con: takes a list and inserts commas and 'and' and outputs a string

def commaCode(values):
    s = ''
    for i in range(0, len(values) - 1):
        s += str(values[i]) + ', '
    s += 'and ' + str(values[len(values) - 1])
    return s

values = [1, 2, 3, 4]
result = commaCode(values)
print(result)
