#!/usr/bin/python3


def element_at(my_list, idx):
    if idx < 0:
        return ("None")

    for i in range(len(my_list)):
        if idx > len(my_list):
            return ("None")
        return (my_list[idx])
