#! python3
# delFiles.py- walks through a folder tree and 
# searches for exceptionally large files or folders ,
# printing those files with their absolute path 

import shutil, os
from pathlib import Path

source = Path('F:\\STUDY')
largesize = 524288000
largefiles = []
largefilessize = []
def delunneededfiles(source):
    
    #Walking through the source folder tree
    for foldername, subfolders, filenames in os.walk(source):
        for file in filenames:
            file_size = os.path.getsize(os.path.join(foldername, file))
            file_path = os.path.join(foldername, file)
            
            if file_size > largesize:
                largefiles.append(file_path)
                largefilessize.append(file_size)
    
delunneededfiles(source)

for largefile, largefilesize in zip(largefiles, largefilessize):
        print(f'{largefile}- {largefilesize}')