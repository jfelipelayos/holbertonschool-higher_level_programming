#!/usr/bin/python3
def multiple_returns(sentence):

    if not sentence:
        return(0, None)

    size = len(sentence)

    first_character = sentence[0]

    return(size, first_character)
