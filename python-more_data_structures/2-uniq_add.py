#!/usr/bin/python3


def uniq_add(my_list=[]):

    new_list = []
    sum = 0

    for number in my_list:
        if number not in new_list:
            new_list.append(number)
            sum += number

    return (sum)

