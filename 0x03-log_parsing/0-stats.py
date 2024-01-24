#!/usr/bin/python3
"""
log parsing
"""

import sys

if __name__ == "__main__":
    filesize, cnt = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    states = {k: 0 for k in codes}

    def print_states(states: dict, file_size: int) -> None:
        """print states"""
        print("File size: {:d}".format(file_size))
        for k, v in sorted(states.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            cnt += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in states:
                    states[status_code] += 1
            except BaseException:
                pass
            try:
                filesize += int(data[-1])
            except BaseException:
                pass
            if cnt % 10 == 0:
                print_states(states, filesize)
        print_states(states, filesize)

    except KeyboardInterrupt:
        print_states(states, filesize)
        raise
