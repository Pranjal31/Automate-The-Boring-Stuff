#!python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

# phone number pattern not including extension
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?      # optional area code 
    (-|\s|\.)?              # optioal separator
    (\d{3})                 # 3 digits (after the area code)
    (-|\s|\.)               # separator
    (\d{4})                 # last 4 digits
    )''', re.VERBOSE)

# email address pattern
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # '@' symbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4})        # dot-something (TLD)
    )''', re.VERBOSE)

# find all matches in clipboard text
text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    matches.append(phoneNum)

for email_match in emailRegex.findall(text):    
    matches.append(email_match[0])

# copy results to the clipboard
if len(matches) > 0:
    result = '\n'.join(matches)
    pyperclip.copy(result)
    print('Copied to clipboard:')
    print(result)
else:
    print('No phone numbers or email addresses found.')



''' 
Testing :
Open your web browser to the No Starch Press contact page at https://nostarch.com/contactus/, press CTRL-A to select all the text on the page, and press CTRL-C to copy it to the clipboard.
Run the program.
'''