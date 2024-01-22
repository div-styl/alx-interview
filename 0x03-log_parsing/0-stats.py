#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics
"""
import sys


def print_stats(code, filesize):
    """Prints statistics"""
    print("file size: {}".format(filesize))
    for k, val, in sorted(code.items()):
        if val != 0:
            print("{}: {}".format(k, val))


file_size = 0
code = 0
count_lines = 0
codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
    }

try:
    for line in sys.stdin:
        parese_lines = line.split()
        parese_lines = parese_lines[::-1]

        if len(parese_lines) > 2:
            count_lines += 1

            if count_lines <= 10:
                file_size += int(parese_lines[0])
                code = parese_lines[1]

                if (code in codes.keys()):
                    codes[code] += 1
            if (count_lines == 10):
                print_stats(codes, file_size)
                count_lines = 0

finally:
    print_stats(codes, file_size)
