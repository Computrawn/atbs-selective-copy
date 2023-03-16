#! python3
"""selective_copy.py — An exercise in organizing files.
For more information, see enclosed project_details.txt file."""

import os
import re
import shutil

file_list = []


def selective_copy(file_path):
    """Walk through folder tree, search for files with user-defined file extension,
    then copy those files to a user-defined folder."""

    ext_regex = re.compile(r"(.*)\." + (input("Type desired file extension here: ")))
    new_folder = input(f"Please type path to destination folder: ")
    relocation_folder = f"{os.getcwd()}/{new_folder}"

    for folder_name, subfolders, filenames in os.walk(file_path):
        for filename in filenames:
            absolute_path = f"{os.getcwd()}/{folder_name}/{filename}"
            mo = ext_regex.search(absolute_path)
            if mo is not None:
                file_list.append(mo.group())

    length = len(file_list)
    print(f"Found {length} matches.")

    for match in range(length):
        print(f"Moving {file_list[match]} to {relocation_folder}.")
        shutil.move(file_list[match], relocation_folder)


folder_path = input("Type path to folder you wish to search here: ")
selective_copy(folder_path)
