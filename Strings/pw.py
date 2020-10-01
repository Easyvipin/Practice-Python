#! python3
# password locker

import sys
import pyperclip


passwords = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'
             }
if len(sys.argv) < 2:
    print(' Usage : pw.py [account] -- to copy the password')
    sys.exit()

account = sys.argv[1]
if account in passwords:
    pyperclip.copy(passwords[account])
    print(f"Password is copied to the clipboard of {account}")
else:
    print(f"{account} not found ")

 # >> py pw.py email
# Password is copied to the clipboard of email
