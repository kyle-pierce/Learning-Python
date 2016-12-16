# outputs the number of occurances of each character in the message
import pprint

message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
           Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure \
           dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, \
           sunt in culpa qui officia deserunt mollit anim id est laborum.'

count = {}

for character in message:
    character = character.lower()
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
