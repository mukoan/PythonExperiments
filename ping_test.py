#!/usr/bin/env python3
# File  : ping_test.py
# Author: Lyndon Hill

"""Example for getting ping information and also string parsing.

Arguments:
target IP address/domain name (optional)
"""

import sys
import subprocess

def main():
    """Main entry point to script."""
    print("Ping test")

    ip_target = "127.0.0.1"
    if len(sys.argv) > 1:
        ip_target = sys.argv[1]

    number_pings = 10
    print("Test starting, pinging ip", ip_target)

    # Ping the ip address
    ping_output = subprocess.run(["ping", ip_target, "-c" + str(number_pings)],
                                 capture_output=True)

    ping_result = ping_output.stdout.decode(sys.stdout.encoding)
    ping_by_lines = ping_result.split('\n')

    packets_received = 0

    for line in ping_by_lines:
        # Alternatively, use a regex instead of the following
        packet_details = line.split()
        if len(line) >= 2 and packet_details[1] == "bytes":
            time_substring = packet_details[-2]  # Last part of string is "... time=s.dd ms"
            time_timepart = time_substring.split('=')
            print("Time =", time_timepart[-1])
            packets_received += 1

    print("%d packets received" % packets_received)
    print("Done.")

if __name__ == '__main__':
    main()
