#!/usr/bin/python3


def multiple_returns(sentence):

    if len(sentence) == 0:
        character = None
    else:
        character = sentence[0]

    return (len(sentence), character)
