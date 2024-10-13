#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, bs4, os

URL_BASE = 'https://xkcd.com'
url = URL_BASE
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # Download the page
    print("Downloading page " + url)
    res = requests.get(url)
    res.raise_for_status()

    # Get the URL of the comic image
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('#comic img')

    if len(comicElem) == 0:
        print('Could not find comic image')
    imgUrl = 'https:' + comicElem[0].get('src')

    # Download the image and save it to ./xkcd
    print("Downloading image " + imgUrl)
    res = requests.get(imgUrl)
    res.raise_for_status()

    imageFile = open(os.path.join('xkcd', os.path.basename(imgUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # Get the Prev button's url
    prevElem = soup.select('a[rel="prev"]')[0]
    url = URL_BASE + prevElem.get('href')

print("Done")