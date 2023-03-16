#! python3
# selective_copy.py — An exercise in organizing files.
# For more information, see enclosed project_details.txt file.

import os
import re
import shutil


def selective_copy(file_path):
    # TODO: Walk through folder tree.
    for folder_name, subfolders, filenames in os.walk(file_path):
        print(f"The current folder is {folder_name}")

        for subfolder in subfolders:
            print(f"Subfolder of {folder_name}: {subfolder}")

        for filename in filenames:
            print(f"File inside {folder_name}: {filename}")

    # TODO: Search for files with certain file extensions.

    # TODO: Copy files from current location to a new folder.


selective_copy(input("Type path to folder you wish to search here: "))
