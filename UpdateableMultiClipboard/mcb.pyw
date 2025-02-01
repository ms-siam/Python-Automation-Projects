#! python3
#mcb.pyw - Saves and loads pieces of text to the clipboard.
#Usage:py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#      py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#      py.exe mcb.pyw list - Loads all keywords to clipboard.

import pyperclip, shelve, sys

with shelve.open('mcb') as mcbShelf:

      #Todo: Save clipboard content.
      
      
      #Todo: List keywords and load content.
      