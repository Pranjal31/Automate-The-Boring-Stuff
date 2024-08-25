#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments

import zipfile, os, sys
from pathlib import Path

def backupToZip(folder):
    # Back up the entire contents of "folder" into a ZIP file
    folderPath = Path(folder).absolute()  # make sure folder is absolute


    # Figure out the filename this code should use
    number = 1
    while True:
        zipFilename = folderPath.name + f'_{number}.zip'
        if not Path(zipFilename).exists():
            break
        number += 1

    # Create the ZIP file
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(str(folderPath)):
        print(f'Adding files in {foldername}...')

        # Add current folder to the ZIP file
        backupZip.write(foldername)
        
        # Add all the files in this folder to the ZIP file
        for filename in filenames:
            newBase = folderPath.name + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                print(f'Skipping backup of ZIP file {filename}')
                continue      # don't back up the backup ZIP files
            backupZip.write(Path(foldername) / Path (filename))
    backupZip.close()
    print('Backup complete')

if len(sys.argv) != 2:
    print("Usage: python backupToZip.py <folder_path>")
    sys.exit(1)

folder = sys.argv[1]
backupToZip(folder)
    