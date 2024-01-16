#!/usr/bin/python3
"""minimum operations"""


def minOperations(n):
    """minimum operations"""
    if n <= 2:
        return 0
    op, count = 0, 2
    while count <= n:
        if n % count == 0:
            op += count
            n /= count
            count -= 1
        count += 1
    return op
