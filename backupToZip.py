#! python3
# f-strings are only compatible with Python >= 3.6
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

# For anyone using the script: replacer folder_X with the desired variable names and replace the part where 
# it says /Insert/PathX/Here with the paths to the folders that need to be backed up. 
# The script might need to be run with the Python3 <script name> command before being executed,
# as Python <script name> will run the pre-installed Python on MacOS. Only Python 3 is compatible. 


import os
import shutil
import zipfile
from pathlib import Path

# Back up the entire contents of "folder" into a ZIP file.


def backupToZip(folder):

    folder = os.path.abspath(folder)   # make sure folder is absolute

    # Delete old zipfile, because only one backup is needed at a time
    zipFilename = os.path.basename(folder) + '.zip'
    if os.path.exists(zipFilename):
        os.unlink(f'{os.getcwd()}/{zipFilename}')
        print(f'Deleted old {folder}/{zipFilename}')

    # TODO: Create the ZIP file.
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # TODO: Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            if filename.endswith('.zip'):
                continue   # don't back up the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')


# Windows Format: backupToZip('C:\\delicious')
folder_1 = Path.home()/'Insert/Path1/Here'
backupToZip(folder_1)

folder_2 = Path.home()/'Insert/Path2/Here'
backupToZip(folder_2)

folder_3 = Path.home()/'Documents/Taxes'
backupToZip(folder_3)
