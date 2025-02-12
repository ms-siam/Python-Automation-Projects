#! python3
# downloadXkcd.py- Downloads every single XKCD comic.

import requests, os, bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    #Download the page
    print(f'Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    
    #Find the url of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
    #Download the image
    
    #Save the image to ./xkcd
    
    #Get the Prev button's url
    