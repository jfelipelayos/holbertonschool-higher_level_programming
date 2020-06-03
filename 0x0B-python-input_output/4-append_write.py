#!/usr/bin/python3
"""append write module
    """


def append_write(filename="", text=""):
    """Append text to a file

    Args:
        filename (str, optional): File name. Defaults to "".
        text (str, optional): Text to append. Defaults to "".

    Returns:
        int: Number of characters added
    """

    with open(filename, mode='a', encoding='utf8') as a_file:
        a_file.write(text)
    return (len(text))
