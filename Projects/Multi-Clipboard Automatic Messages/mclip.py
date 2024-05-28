#! python3
#mclip.py - A multi-clipboard program

import sys, pyperclip

TEXT = {'busy': "Sorry, can we do this later this week or next week?",
        'agree': "Yes, I agree. That sounds fine to me.",
        'defer': "Can I get back to you on this later?"
        }

if len(sys.argv) < 2:
    print("Usage: ./mclip.py [keyphrase] - copy phrase text")
    sys.exit()

keyphrase = (sys.argv[1]).lower()

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f"Text for keyphrase '{keyphrase}' copied")
else:
    print(f"there is no text for keyphrase '{keyphrase}'")