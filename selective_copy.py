#! python3
"""selective_copy.py — An exercise in organizing files.
For more information, see enclosed project_details.txt file."""

import os
import re
import shutil

file_list = []


def selective_copy(file_path):
    """Walk through folder tree, search for files with user-defined file extension,
    then copy those files to a user-defined directory."""

    ext_regex = re.compile(r"(.*)\." + (input("Type desired file extension here: ")))
    copy_dir = input("Please type path to destination existing directory: ")

    for dir_name, subfolders, filenames in os.walk(file_path):
        for filename in filenames:
            absolute_path = f"{dir_name}/{filename}"
            match_object = ext_regex.search(absolute_path)
            if match_object is not None:
                file_list.append(match_object.group())

    length = len(file_list)
    print(f"Found {length} matches: {file_list}.")

    try:
        for match in range(length):
            print(f"Copying {file_list[match]} to {copy_dir}.")
            shutil.copy(file_list[match], copy_dir)
    except FileNotFoundError:
        print("Unable to transfer files; directory not found.")


dir_path = input("Type path to directory you wish to search here: ")
selective_copy(dir_path)
