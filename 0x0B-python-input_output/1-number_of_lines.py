#!/usr/bin/python3
"""Number of lines module
    """


def number_of_lines(filename=""):
    """Find number of lines in a file

    Args:
        filename (str, optional): File to count lines. Defaults to "".

    Returns:
        int: number of lines
    """

    count = 0
    with open(filename) as a_file:
        for line in a_file:
            count += 1
    return count
