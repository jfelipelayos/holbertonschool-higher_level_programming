#!/usr/bin/python3
"""Read file module
    """


def read_file(filename=""):
    """Read file

    Args:
        filename (str, optional): File to print. Defaults to "".
    """

    with open(filename, encoding='utf-8') as a_file:
        for line in a_file:
            print(line, end="")
    print()
