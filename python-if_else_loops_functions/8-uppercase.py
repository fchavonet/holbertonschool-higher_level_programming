#!/usr/bin/python3


def uppercase(str):
    for character in str:
        if 'a' <= character <= 'z':
            uppercase_character = chr(ord(character) - 32)
        else:
            uppercase_character = character
        print(uppercase_character, end="")
    print()
