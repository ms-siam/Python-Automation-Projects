#! python3
# delFiles.py- walks through a folder tree and 
# searches for exceptionally large files or folders ,
# printing those files with their absolute path 

import shutil, os
from pathlib import Path

source = Path('F:\\STUDY')
size = []
largesize = 524,288,000
fileno = 0
files = []
largefiles = []
largefilesize = []
def delunneededfiles(source):
    
    #Walking through the source folder tree
    for foldername, subsolders, filenames in os.walk(source):
        for file in filenames:
            size.append(os.path.getsize(file))
            files.append(os.path.abspath(file))
            fileno = fileno + 1
        if int(size[fileno]) > largesize:
            largefiles.append(files[fileno])
            largefilesize.append(size[fileno])
for i in largefiles:
    print(f'')