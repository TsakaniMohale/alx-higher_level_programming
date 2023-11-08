#!/usr/bin/python3

if __name__ == "__main__":
    """print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} arguments:".format(count))
    else:
        print("{} arguments:".format(count))

    if count >= 1:
        count = 0
        for arg in sys.argv:
            if count != 0:
                print("{}: {}".format(count, arg))
            count += 1
