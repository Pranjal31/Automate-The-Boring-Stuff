#! python3
# How to keep an idiot busy for hours

import pyinputplus as pyip

while True:
    response = pyip.inputYesNo(prompt='Want to know how to keep an idiot busy for hours?\n', caseSensitive=False)
    if response == 'no':
        break
print('Thank you. Have a nice day.')
