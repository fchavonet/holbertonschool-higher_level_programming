#!/usr/bin/python3

"""
Module with a function that prints a text with 2 new lines
after each of these characters: `.`, `?` and `:`.
"""


def text_indentation(text):
    """
    prints a text with 2 new lines
    after each of these characters: `.`, `?` and `:`.

    Args:
    text (str): The input text to be print.

    Raises:
    TypeError: If the input `text` is not a string.
    """

    if type(text) is not (str):
        raise TypeError("text must be a string")

    sentence = ""

    for letter in text:

        sentence += letter

        if letter in [".", "?", ":"]:
            print("{}\n".format(sentence.strip()))
            sentence = ""

    if sentence.strip() != "":
        print(sentence.strip())
