#!/usr/bin/env python3
# File  : chooser.py
# Author: Lyndon Hill

""" Example for choosing an output by random selection."""

import random

def main():
    """Main entry point to script."""
    print("Chooser test")

    # Choose a meal randomly from the list
    meals = ["spaghetti alla arrabiata", "pizza", "gang keow wan",
             "fajitas", "vegetable biriyani", "chili con carne",
             "pad thai", "dhal", "yasai yakisoba"]
    print("Today, let's make", random.choice(meals))

    # Choose a random number between 1 and 20
    print("Random number =", random.randint(1, 20))

    print("Done.")

if __name__ == '__main__':
    main()
