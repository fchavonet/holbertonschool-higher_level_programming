#!/usr/bin/python3new_list


def search_replace(my_list, search, replace):

    new_list = my_list.copy()

    for number in range(len(new_list)):
        if new_list[number] == search:
            new_list[number] = replace

    return new_list
