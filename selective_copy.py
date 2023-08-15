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
logging.disable(logging.CRITICAL)  # Note out to enable logging.


def validate_directory() -> Path:
    """Check user input to determine path validity."""
    directory = Path(input("Please type path of directory you wish to search: "))
    if not directory.exists():
        raise AttributeError
    return directory


def find_files(directory: Path) -> list[str]:
    """Walk through directory tree and create list of files matching user-defined extension."""
    extension = input("Type extension you want to find here: ").lower()
    file_list = [
        f"{dir_name}/{filename}"
        for dir_name, _, filenames in os.walk(directory)
        for filename in filenames
        if filename.endswith(f".{extension}")
    ]
    """Notify user of match results."""
    if len(file_list) == 1:
        print(f"Found {len(file_list)} file ending in .{extension}.")
    elif len(file_list) > 1:
        print(f"Found {len(file_list)} files ending in .{extension}.")
    else:
        print(f"No files of extension type .{extension} found.")
    return file_list


def verify_copy_folder() -> Path:
    """Create copy directory if path doesn't exist."""
    copy_directory = Path(input("Please type path of existing directory: "))
    if not copy_directory.exists():
        os.mkdir(copy_directory)
    return copy_directory


def move_files(files_to_move: list[str], new_location: Path) -> None:
    """Move files to user-designated path"""
    for file_path in files_to_move:
        file_name = file_path.split("/")
        print(f"— Copying {file_name[-1]} to {new_location}.")
        shutil.copy(file_path, new_location)


def main() -> None:
    """Validate directory, search folders for extensions and copy matching files to designated folder."""
    try:
        directory = validate_directory()
        file_list = find_files(directory)
        if file_list:
            copy_location = verify_copy_folder()
            move_files(file_list, copy_location)
    except AttributeError:
        print("Not a valid directory.")


if __name__ == "__main__":
    main()
