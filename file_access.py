#!/usr/bin/env python3
# File  : file_access.py
# Author: Lyndon Hill

"""Example for getting information on filesystem.

Arguments:
filename/directory name (optional)
"""

import sys
import os

def main():
    """Main entry point to script."""
    print("File access test")

    if len(sys.argv) >= 2:
        file_name = sys.argv[1]
    else:
        file_name = "README.md"

    print("Getting info on " + file_name)

    # File and directory tests
    is_file = os.path.isfile(file_name)
    is_directory = os.path.isdir(file_name)
    if is_file:
        print(file_name + " is a file")
    if is_directory:
        print(file_name + " is a directory")

    # Get file attributes
    info = os.stat(file_name)
    print("User identifier for file owner: " + str(info.st_uid))
    print("Size of file (b): " + str(info.st_size))
    print("Last modification time: " + str(info.st_mtime))
    print("File attributes: " + str(oct(info.st_mode)))

    print("Done.")

if __name__ == '__main__':
    main()
