#!/usr/bin/env python3
# File  : arguments.py
# Author: Lyndon Hill

"""Example for accessing arguments from shell."""

import sys

def main():
    """Main entry point to script."""
    print("Argument test")
    print("%d arguments:" % (len(sys.argv)))

    for arg in sys.argv:
        print("argument <" + arg + ">")

    print("Done.")

if __name__ == '__main__':
    main()
