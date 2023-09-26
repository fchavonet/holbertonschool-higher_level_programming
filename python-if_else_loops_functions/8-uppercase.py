#!/usr/bin/python3


def uppercase(str):
    for character in str:
        if ord('a') <= ord(character) <= ord('z'):
            uppercase_character = chr(ord(character) - 32)
        else:
            uppercase_character = character
        print("{}".format(uppercase_character), end="")
    print()
