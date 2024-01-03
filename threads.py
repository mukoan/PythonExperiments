#!/usr/bin/env python3
# File  : threads.py
# Author: Lyndon Hill

"""Example for using multiple threads."""

import threading

def simple_output(msg):
    """This is an example simple function."""
    print("Simple message =", msg)

def complex_output(number):
    """Imagine this is a complex function; it is more complex than simple_output()."""
    result = 0
    for i in range(0, 10):
        for j in range(0, number):
            result += 1000*1000
            result += j
        print("Complex iteration %d" % i)

def main():
    """Main entry point to script."""
    print("Multithreading test")

    thread1 = threading.Thread(target=complex_output, args=(1000,))
    thread2 = threading.Thread(target=simple_output, args=("Felicitations",))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Done.")

if __name__ == '__main__':
    main()
