#!/usr/bin/env python3
# File  : external_command.py
# Author: Lyndon Hill

""" Example for running an external shell command."""

import subprocess
import os

def main():
    """Main entry point to script."""
    print("External command test")

    # Run an external command and capture its output
    cmd_output = subprocess.run(["ls", "-1"], capture_output=True)
    print("External command output captured as:\n", cmd_output.stdout)

    # Capture a environmental variable
    print("Environmental variable $USER =", os.environ["USER"])

    # Set an environmental variable
    # Note: eons ago there was a security thing where if someone left
    #       their computer logged in you would send "I like sheep" as a
    #       message from their user
    os.environ["SHEEP"] = "like"
    print("Environmental variable $SHEEP was set to: ", os.environ["SHEEP"])

    print("Done.")

if __name__ == '__main__':
    main()
