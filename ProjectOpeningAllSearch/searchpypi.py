#! python3
# searchpypi.py- Opens several search results.

import requests, sys, webbrowser, bs4 # type: ignore

print('Searching...')      # Display text while downloading the search result
res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#Todo: Retrieve the top search results

soup = bs4.BeautifulSoup(res.text, 'html.parser')

#Todo: Open a browser tab for each results

linkElems = soup.select('.package-snippet')

numOpen = min(5, len(linkElems))