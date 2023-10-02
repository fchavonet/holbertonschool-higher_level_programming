#!/usr/bin/python3


def element_at(my_list, idx):

    my_list_length = len(my_list)

    if idx < 0 or idx > my_list_length - 1:
        return ("None")
    return (my_list[idx])
