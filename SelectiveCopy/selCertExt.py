#! python3
# selCertExt.py- walks through a folder tree, then searches for a certain
# file extension like '.py', '.jpg' etc and copy them to a new folder 

import shutil, re, os
from pathlib import Path


source = Path('C:\\Users\\Mobarok Siam\\Desktop')
extension = '.jpg'
destination = (source / extension.lstrip('.'))
destination.mkdir(exist_ok=True)

def selandcopyfiles(source, destination, ext):
    # Walking through the folder tree
    for foldername, subfolders, filenames in os.walk(source):
        # Searching for a certain file extension
        for filename in filenames:
            if not filename.endswith(ext):
                continue
            shutil.copy(Path(foldername) / filename, destination/filename)




# Copy them to a new folder