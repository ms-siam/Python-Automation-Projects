#! python3
# downloadXkcd.py- Downloads every single XKCD comic.

import requests, os, bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    #Download the page
    
    #Find the url of the comic image
    
    #Download the image
    
    #Save the image to ./xkcd
    
    #Get the Prev button's url
    