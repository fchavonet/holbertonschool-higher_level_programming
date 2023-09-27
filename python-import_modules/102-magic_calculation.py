#!/usr/bin/python3


def magic_calculation(a, b):
    if a < b:
        result = a + b
        for i in range(4, 6):
            result += i
        return result
    else:
        return a - b
