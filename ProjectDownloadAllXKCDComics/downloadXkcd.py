#! python3
# downloadXkcd.py- Downloads every single XKCD comic.

import requests, os, bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)