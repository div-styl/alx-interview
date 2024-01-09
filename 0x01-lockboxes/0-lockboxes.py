#!/usr/bin/python3
"""a method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened."""
    for k in range(1, len(boxes)):
        flag = False
        for box in range(len(boxes)):
            if k in boxes[box] and box != k:
                flag = True
                break
        if not flag:
            return False
    return True
