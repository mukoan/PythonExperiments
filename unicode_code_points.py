#!/usr/bin/env python3
# File  : unicode_code_points.py
# Author: Lyndon Hill

"""Example for handling UniCode code points."""

import sys

# Check version because this script uses f-strings
assert sys.version_info >= (3, 6)

def main():
    """Main entry point to script."""
    print("UniCode code points test")

    thai_language = "ภาษาไทย"
    thai_no = "ไม่"                # note last character is combining, mai ayk
    japanese_language = "日本語"
    japanese_no = "いいえ"

    print("Length of Thai Language =", len(thai_language))  # expected result 7
    print("Length of Thai no =", len(thai_no)) # expected result 3
    print("Length of Japanese Language =", len(japanese_language)) # expected result 3
    print("Length of Japanese no =", len(japanese_no)) # expected result 3

    print(f"UniCode code point for {thai_language[0]} = {ord(thai_language[0])}")
    print(f"UniCode code point for {japanese_language[0]} = {ord(japanese_language[0])}")

    th_lang_utf16 = thai_language.encode(encoding='utf-16')
    print(f"Thai language in UTF-16 = {th_lang_utf16}")

    ja_lang_utf8 = japanese_language.encode(encoding='utf-8')
    print(f"Japanese language in UTF-8 = {ja_lang_utf8}")

    print("Done.")

if __name__ == '__main__':
    main()
