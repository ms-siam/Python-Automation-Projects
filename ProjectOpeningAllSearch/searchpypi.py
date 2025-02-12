#! python3
# searchpypi.py- Opens several search results.

import requests, sys, webbrowser, bs4 # type: ignore

print('Searching...')      # Display text while downloading the search result
res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))