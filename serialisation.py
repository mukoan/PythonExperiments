#!/usr/bin/env python3
# File  : serialisation.py
# Author: Lyndon Hill

""" Example for serialisation."""

import pickle
from dataclasses import dataclass

@dataclass
class Record:
    """Simple data holding class."""
    title: str
    version: int
    count: int

def main():
    """Main entry point to script."""
    print("Serialisation test")

    # Set up object to serialise
    my_object = Record('oranges', 1, 10)

    fruit_file = open('fruit.txt', 'wb')
    pickle.dump(my_object, fruit_file)
    fruit_file.close()

    check_file = open('fruit.txt', 'rb')
    decoded_object = pickle.load(check_file)
    check_file.close()
    print("Unserialised title = " + decoded_object.title)

    print("Done.")

if __name__ == '__main__':
    main()
