#!/usr/bin/python3


def max_integer(my_list=[]):

    if len(my_list) == 0:
        return (None)

    biggest_number = my_list[0]

    for number in my_list:
        if number > biggest_number:
            biggest_number = number

    return (biggest_number)
