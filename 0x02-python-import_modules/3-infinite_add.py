#!/usr/bin/python3
if __name__ == "__main__":
    """Infinite addition"""
    import sys
    n = len(sys.argv) - 1
    count = 0
    for i in range(n):
        count += int(sys.argv[i + 1])
    print("{}".format(count))
