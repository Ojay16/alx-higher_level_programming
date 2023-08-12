#!/usr/bin/python3

if __name__ == "__main__":
    """prints the number of and the list of arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for j in range(count):
        print("{}: {}".format(j + 1, sys.argv[j + 1])
