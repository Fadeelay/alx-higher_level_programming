#!/usr/bin/python3
if __name__ == "__main__":
    """Print number of arguments and the value of arguments"""
    import sys
    n = len(sys.argv) - 1

    if n == 0:
        print("{} arguments.".format(n))
    elif n >= 1:
        print("{} arguments:".format(n))
        for i in range(1, n + 1):
            print("{}: {}".format(i, sys.argv[i]))
