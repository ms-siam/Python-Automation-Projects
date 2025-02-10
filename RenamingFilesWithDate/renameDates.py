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
    
    #skip files without a date
    if mo == None:
        continue
    
    #Get the different part of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the European Style Filename
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    
    # Get the Full , absolute path
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the Files
    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    #shutil.move(amerFilename, euroFilename)    #uncomment after testing