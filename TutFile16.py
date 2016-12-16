# Text file regex searcher
# Will seach the indicated directory for all occurances of the supplied regular expression

import re, os, pprint

directory = 'C:\\Users\\Kyle\\Desktop\\TestFolder'
files = os.listdir(directory)

def getUserRegex():
    print('For which pattern should I search? ', end = '')
    valid = False
    given_regex = ''

    while (not valid):
        regex = input()
        try:
            given_regex = re.compile(regex)
            valid = True
            print()
            print('Regular Expression accepted!')
            print()
        except re.error:
            valid = False
            print('There was an issue.  Please try again ', end ='')

    return given_regex

regex = getUserRegex()

for f in files:
    text_file = open(directory + '\\' + f)
    text = text_file.read()
    matches = regex.findall(text)
    print('Matches found in ' + f + ': ' + str(matches))
    print()

