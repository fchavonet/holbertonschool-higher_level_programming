#!/usr/bin/python3


def best_score(a_dictionary):

    if a_dictionary is None:
        return (None)

    max_value = 0
    best_key = None

    for key, value in a_dictionary.items():
        if value > max_value:
            best_key = key
            max_value = value

    return (best_key)
