#!/usr/bin/env python3
# File  : json_format.py
# Author: Lyndon Hill

"""Example for handling JSON."""

import os
import json

def main():
    """Main entry point to script."""
    print("JSON test")

    file_name = "christmas.json"

    # If JSON file already exists then load it and parse
    if os.path.isfile(file_name):
        # Found a JSON file
        with open(file_name) as christmas_file:
            christmas_json = json.load(christmas_file)
            print("Loaded and parsed JSON file as", type(christmas_json))
            for key, value in christmas_json.items():
                print(key, ":", value)
            print("Access key 2:", christmas_json["2"])

        print("Done.")
        return

    # Create the JSON data
    json_dict = {"1": "A partridge in a pear tree",
                 "2": "Two turtle doves",
                 "3": "Three French hens",
                 "4": "Four calling birds",
                 "5": "Five golden rings",
                 "6": "Six geese a-laying",
                 "7": "Seven swans a-swimming",
                 "8": "Eight maids a-milking",
                 "9": "Nine ladies dancing",
                 "10": "Ten lords a-leaping",
                 "11": "Eleven pipers piping",
                 "12": "Twelve drummers drumming"}

    # Write data to file
    output_file = open(file_name, 'w')
    json.dump(json_dict, output_file)
    output_file.close()
    print("Wrote JSON file")
    print("Done.")

if __name__ == '__main__':
    main()
