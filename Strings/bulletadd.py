#! python3
# add bullet in front of list copied from web or somewhere else

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')
""" to split the copied string by new line character """

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)

# this file has bat file
