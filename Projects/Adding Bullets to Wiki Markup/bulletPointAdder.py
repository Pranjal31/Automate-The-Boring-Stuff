#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard

import pyperclip

# paste from clipboard
text = pyperclip.paste()

# manipulate text to include bullet points
lines = text.split('\n')  # string to list

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)  # list to string

# copy to clipboard
pyperclip.copy(text)