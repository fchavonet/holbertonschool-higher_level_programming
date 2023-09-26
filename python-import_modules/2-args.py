#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    len_argv = len(argv)

    if len_argv == 1:
        print("0 arguments.")
    elif len_argv == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len_argv - 1))

    for i in range(1, len_argv):
        print("{}: {}".format(i, argv[i]))
