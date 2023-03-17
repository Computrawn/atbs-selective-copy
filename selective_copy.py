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
    relocation_folder = input("Please type path to destination existing folder: ")

    for folder_name, subfolders, filenames in os.walk(file_path):
        for filename in filenames:
            absolute_path = f"{folder_name}/{filename}"
            match_object = ext_regex.search(absolute_path)
            if match_object is not None:
                file_list.append(match_object.group())

    length = len(file_list)
    print(f"Found {length} matches.")

    try:
        for match in range(length):
            print(f"Copying {file_list[match]} to {relocation_folder}.")
            shutil.copy(file_list[match], relocation_folder)
    except FileNotFoundError:
        print("Unable to transfer files; folder not found.")


folder_path = input("Type path to folder you wish to search here: ")
selective_copy(folder_path)
