#!/usr/bin/python3
"""append write module
    """


def append_write(filename="", text=""):

    with open(filename, mode='a', encoding='utf8') as a_file:
        a_file.write(text)
    return (len(text))
