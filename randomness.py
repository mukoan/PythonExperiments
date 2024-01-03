#!/usr/bin/env python3
# File  : randomness.py
# Author: Lyndon Hill

""" Example to compare how random Python random module's PRNG is to numpy's."""

import random
import numpy as np
import matplotlib.pyplot as plt

def main():
    """Main entry point to script."""
    print("Randomness test")

    trials = 100000
    histogram = np.empty(trials+1)
    total = 0

    for i in range(0, trials):
        r = random.randint(1, 100)
        histogram[i] = r
        total += r

    # Get mean
    mean = total/trials

    # Get median
    median = np.median(histogram)

    print("Random number generator from random module")

    # Output stats
    print("Mean = " + str(mean))
    print("Median = " + str(median))

    # Use matplotlib to create a graph
    plt.hist(histogram)
    plt.show()

    # Comparison

    print("Uniform distributed random number generator from numpy module")

    rng = np.random.default_rng(12323234)
    uni_np_dist = rng.integers(low=1, high=100, size=trials)

    plt.hist(uni_np_dist)
    plt.show()

    print("Done.")

if __name__ == '__main__':
    main()
