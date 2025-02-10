#! python3
# backupToZip.py- Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder):
    # Backup the entire contents of 'folder' into a zip file
    folder = os.path.abspath(folder) # make sure folder is absolute path
    
    #Figure out the filename this code should use based on 
    # what files already exist
    
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number+1
        
    # Create the ZIP file
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    
    # Walk the intire folder tree and compress the files in each folder
    
    print('Done')
    
backupToZip('C:\\delicious')