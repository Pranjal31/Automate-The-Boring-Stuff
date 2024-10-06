import webbrowser
import pyperclip
import sys

if len(sys.argv) > 1:
    # get street address from comamnd line args
    st_address = sys.argv[1]
else:
    # get street address from clipboard
    st_address = pyperclip.paste()

# open street address in webbrowser
st_address_list = st_address.replace(' ', '+')
webbrowser.open(f"https://www.google.com/maps/place/{st_address_list}")