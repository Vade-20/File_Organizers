# File_Organizers
This repository contains three Python scripts that can help you organize your files.

### File_organizer_by_type.py
File_organizer_by_type.py creates a new directory called "Organized_folder" and subfolders for each file type found in the current directory. The Python script then moves files to their corresponding subfolders based on their file type.

### File_organizer_by_size.py
File_organizer_by_size.py creates four subfolders in the "Organized_folder" directory based on the size of the files in the current directory. The Python script then moves the files to the appropriate subfolder based on their size.

### copy_files_to_directory.py
copy_files_to_directory.py moves files from the current directory to the "All_the_files". This Python script walk trough the current directory and subfolders and 
moves files present in them to 'All_the_files'.

# Usage
Download the scripts to a directory on your computer.

Move the python scirpts to the directory where you want it to perfom the task.

Open a terminal or command prompt and navigate to the directory where the scripts are located.

# Requirements
Python 3.x

The os, shutil, and send2trash modules (which can be installed using pip)

## Notes
1.The script will not copy directories, only files. 

2.Any files that cannot be copied (e.g. due to permission errors) will be skipped without raising an error.
