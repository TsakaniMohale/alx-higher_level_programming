#!/usr/bin/python3
if __name__ == "__main__":
    """print the addition of all arguments."""
    import sys

    total = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            total += int(arg)
    print(total)
