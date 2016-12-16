#! python3
# pw.py - An insecure passwords manager

PASSWORDS = {'email': 'abc123',
             'blog': 'ihaveablog',
             'luggage': '74569'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python TutFile11.py [account] - copy accound password')
    sys.exit();

account = sys.argv[1]   #first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account names ' + account)
