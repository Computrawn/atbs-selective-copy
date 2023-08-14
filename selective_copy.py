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


"""Needs major refactor. I'm guessing using glob instead of regex would be better."""

# copy_dir = input("Please type path to destination existing directory: ")

directory = Path(input("Please type path of directory you wish to search: "))


def list_files():
    """Walk through directory tree and create list of files."""

    file_list = [
        Path(f"{dir_name}/{filename}")
        for dir_name, _, filenames in os.walk(directory)
        for filename in filenames
    ]
    return file_list


def find_extensions(files):
    extension = glob.glob("*.txt")
    if extension in files:
        print(extension)
    # length = len(file_list)
    # print(f"Found {length} matches: {file_list}.")

    # try:
    #     for match in range(length):
    #         print(f"Copying {file_list[match]} to {copy_dir}.")
    #         shutil.copy(file_list[match], copy_dir)
    # except FileNotFoundError:
    #     print("Unable to transfer files; directory not found.")


file_list = list_files()
for file_name in file_list:
    logging.debug(file_name)
# find_extensions(file_list)
