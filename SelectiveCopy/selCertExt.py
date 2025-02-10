#! python3
# selCertExt.py- walks through a folder tree, then searches for a certain
# file extension like '.py', '.jpg' etc and copy them to a new folder 

import shutil, re, os
from pathlib import Path

# Walking through the folder tree
source = Path('C:\\Users\\Mobarok Siam\\Desktop')
extension = '.jpg'
destination = (source / extension.split('.'))
def selandcopyfiles(source, destination, ext):
    

# Searching for a certain file extension


# Copy them to a new folder