#!/usr/bin/python3
"""write file module
    """


def write_file(filename="", text=""):
    """Write in a file

    Args:
        filename (str, optional): Name of the file. Defaults to "".
        text (str, optional): Text to write on the file. Defaults to "".
    """

    with open(filename, mode='w', encoding='utf8') as a_file:
        a_file.write(text)
    return(len(text))
