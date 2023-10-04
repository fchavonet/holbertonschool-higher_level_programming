#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):

    elements_number = 0

    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except Exception as e:
            continue
        else:
            elements_number += 1
    print()

    return elements_number
