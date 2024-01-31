#!/usr/bin/python3
"""
method that determines if a given data set
represents a valid UTF-8 encoding
"""

def validUTF8(data):
    """
    method that determines if a given data set
    represents a valid UTF-8 encoding
    """
    expected_continuation = 0
    UTF8_BIT_1 = 1 << 7
    UTF8_BIT_2 = 1 << 6
    for value in data:
        mask = 1 << 7
        if expected_continuation == 0:
            while mask & value:
                expected_continuation += 1
                mask = mask >> 1
            if expected_continuation == 0:
                continue
            if expected_continuation == 1 or\
                  expected_continuation > 4:
                return False
        else:
            if not (value & UTF8_BIT_1 and not (value & UTF8_BIT_2)):
                return False
        expected_continuation -= 1
    if expected_continuation == 0:
        return True
    else:
        return False