#! python3
# renameDates.py - Rename Filenames with American MM-DD-YYYY date 
# format to European DD-MM-YYYY

import shutil, os, re

#Create a regex that matches files with the American date format

datePattern = re.compile(r"""^(.*?)
                         ((0|1)?\d)-
                         ((0|1|2|3)?\d)-
                         ((20|25)\d\d)
                         (.*?)$
                         """, re.VERBOSE)

# ToDo- Loop Over the Files in the working directory 

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

# ToDo- skip files without a date


# ToDo- Get the different part of the filename


# ToDo- Form the European Style Filename


# ToDo- Get the Full , absolute path


# ToDo- Rename the Files
