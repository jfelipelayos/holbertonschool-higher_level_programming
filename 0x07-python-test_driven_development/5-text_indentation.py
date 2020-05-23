#!/usr/bin/python3
"""
text indentation
"""


def text_indentation(text):
    """print 2 new lines when find . ? :

    Arguments:
        text {str} -- text to print
    """
    if type(text) not in [str]:
        raise TypeError('text must be a string')

    size = len(text)
    tmp = '.'

    for i in range(size):
        if text[i] == ' ' and tmp in ['.', '?', ':']:
            continue
        if text[i] in ['.', '?', ':']:
            print("{}".format(text[i]), end="")
            print('\n')
        else:
            print("{}".format(text[i]), end="")
        tmp = text[i]
