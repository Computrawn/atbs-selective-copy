#!/usr/bin/env python3
# selective_copy.py — An exercise in organizing files.
# For more information, see README.md

from pathlib import Path
import glob
import logging
import os
import shutil

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
# logging.disable(logging.CRITICAL)  # Note out to enable logging.


# copy_dir = input("Please type path to destination existing directory: ")


def validate_directory():
    directory = Path(input("Please type path of directory you wish to search: "))
    if directory.exists():
        return directory
    else:
        raise AttributeError


def list_files(directory):
    """Walk through directory tree and create and return list of files. If list is empty, raise error."""

    file_list = [
        f"{dir_name}/{filename}"
        for dir_name, _, filenames in os.walk(directory)
        for filename in filenames
    ]
    return file_list


def find_extensions(files):
    extension = input("Type extension you want to find here: ")
    files_found = [
        file_name for file_name in files if file_name.endswith(f".{extension}")
    ]
    return files_found

    # length = len(file_list)
    # print(f"Found {length} matches: {file_list}.")

    # try:
    #     for match in range(length):
    #         print(f"Copying {file_list[match]} to {copy_dir}.")
    #         shutil.copy(file_list[match], copy_dir)
    # except FileNotFoundError:
    #     print("Unable to transfer files; directory not found.")


directory = validate_directory()
file_list = list_files(directory)
found_files = find_extensions(file_list)
for filename in found_files:
    print(filename)

# def main():
#     try:
#         directory = validate_directory()
#         file_list = list_files(directory)
#         logging.debug(file_list)
#         # find_extensions(file_list)
#     except AttributeError:
#         print("Not a valid directory.")


# if __name__ == "__main__":
#     main()
