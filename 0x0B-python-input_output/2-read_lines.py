#!/usr/bin/python3
"""read lines module
    """


def read_lines(filename="", nb_lines=0):
    """Read and print specified lines

    Args:
        filename (str, optional): Name of the file. Defaults to "".
        nb_lines (int, optional): Number of lines to print. Defaults to 0.
    """

    with open(filename, encoding='utf-8') as a_file:

        if nb_lines > 0:
            for i in range(nb_lines):
                line = a_file.readline()
                print(line, end="")
        else:
            line = a_file.read()
            print(line, end="")
