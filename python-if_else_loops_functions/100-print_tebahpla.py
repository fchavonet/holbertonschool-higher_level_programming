#!/usr/bin/python3

if __name__ == "__main__":

    for i in range(122, 96, -1):
        ascii_code = i
        if (i % 2) != 0:
            ascii_code = ascii_code - 32

        print('{:c}'.format(ascii_code), end='')
