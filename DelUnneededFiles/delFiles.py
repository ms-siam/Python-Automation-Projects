#! python3
# delFiles.py- walks through a folder tree and 
# searches for exceptionally large files or folders ,
# printing those files with their absolute path 

import shutil, os
from pathlib import Path

source = Path('F:\\STUDY')
size = []

def delunneededfiles(source, size):
    
    #Walking through the source folder tree
    for foldername, subsolders, filenames in os.walk(source):
        for file in filenames:
            size.append(os.path.getsize(file))

