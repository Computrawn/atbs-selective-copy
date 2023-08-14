#!/usr/bin/env python3
# selective_copy.py — An exercise in organizing files.
# For more information, see README.md

from pathlib import Path
import logging
import os
import shutil

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
# logging.disable(logging.CRITICAL)  # Note out to enable logging.


def validate_directory() -> Path:
    """Check user input to determine path validity."""
    directory = Path(input("Please type path of directory you wish to search: "))
    if not directory.exists():
        raise AttributeError
    return directory


def find_files(directory: Path) -> list[str]:
    """Walk through directory tree and create list of files matching user defined extension."""
    extension = input("Type extension you want to find here: ")
    file_list = [
        f"{dir_name}/{filename}"
        for dir_name, _, filenames in os.walk(directory)
        for filename in filenames
        if filename.endswith(f".{extension}")
    ]
    """Notify user if matches found."""
    if len(file_list) == 1:
        print(f"Found {len(file_list)} file ending in .{extension}.")
    elif len(file_list) > 1:
        print(f"Found {len(file_list)} files ending in .{extension}.")
    else:
        print(f"No files of extension type {extension} found.")
    return file_list


def move_files(files_to_move: list[str]) -> None:
    """Move files to user-designated path"""
    copy_directory = Path(input("Please type path of existing directory: "))
    try:
        for filename in files_to_move:
            print(f"Copying {filename} to {copy_directory}.")
            shutil.copy(filename, copy_directory)
    except FileNotFoundError:
        print("Unable to transfer files; directory not found.")


def main() -> None:
    """Validate directory, search folders for extensions and copy matching files to designated folder."""
    try:
        directory = validate_directory()
        file_list = find_files(directory)
        if file_list:
            move_files(file_list)
    except AttributeError:
        print("Not a valid directory.")


if __name__ == "__main__":
    main()
