#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
''' Usage: 
       ./mcb.py save <keyword> - Saves clipboard text to keyword\n
       ./mcb.py <keyword> - loads keyword's text to clipboard\n
       ./mcb.py list - lists all keywords to clipboard'''

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 2:
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    else:
        print('''Keyword not found.\nUsage: ./mcb.py save <keyword> - Saves clipboard text to keyword\n
       ./mcb.py <keyword> - loads keyword's text to clipboard\n
       ./mcb.py list - lists all keywords to clipboard''')
elif len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcbShelf[sys.argv[2]] = pyperclip.paste()
else:
    print('''Invalid argument(s).\nUsage: ./mcb.py save <keyword> - Saves clipboard text to keyword\n
       ./mcb.py <keyword> - loads keyword's text to clipboard\n
       ./mcb.py list - lists all keywords to clipboard''')
mcbShelf.close()