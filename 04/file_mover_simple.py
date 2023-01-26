import os
import shutil

# specify the source and destination folder paths
src_folder = '/Users/tuomaskivioja/Desktop/test_folder_2/'
dst_folder = '/Users/tuomaskivioja/Desktop/test_folder_1/'

# get a list of all files in the source folder
files = os.listdir(src_folder)

# iterate through the list of files
for file in files:
    # construct the full file path for the current file
    # pic.png
    src_path = os.path.join(src_folder, file)
    dst_path = os.path.join(dst_folder, file)
    # move the file from the source to the destination
    shutil.move(src_path, dst_path)