def add_integer(a, b=98):
    """Add two integers

    Arguments:
        a {int} -- Integer to add

    Keyword Arguments:
        b {int} -- Integer to add (default: {98})

    Raises:
        TypeError: If the first argument itsn't an int or float print error
        TypeError:If the second argument itsn't an integer or float print error

    Returns:
        Int -- Add of the two integers
    """

    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')

    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    a = int(a)
    b = int(b)

    return a + b
