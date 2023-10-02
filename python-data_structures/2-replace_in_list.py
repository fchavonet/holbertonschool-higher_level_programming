#!/usr/bin/python3


def replace_in_list(my_list, idx, element):

    my_list_length = len(my_list)

    if idx < 0 or idx > my_list_length - 1:
        return (my_list)

    my_list[idx] = element
    return (my_list)
