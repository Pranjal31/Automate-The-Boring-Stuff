#! python3
# searchpypi.py
 
import sys, requests, webbrowser, bs4


if len(sys.argv) < 2:
    print("invalid number of arguments")

SEARCH_URL = "https://pypi.org/search/?q=" + '+'.join(sys.argv[1:])
URL_TO_OPEN_BASE = 'https://pypi.org'

print("Searching...")

res = requests.get(SEARCH_URL)
res.raise_for_status()

# retrieve top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# open a browser tab for each result
linkElems = soup.select('.package-snippet')

numOpen = min(5, len(linkElems))

for i in range(numOpen):
    urltoOpen = URL_TO_OPEN_BASE + linkElems[i].get('href')
    print('Opening ' + urltoOpen)
    webbrowser.open(urltoOpen)
