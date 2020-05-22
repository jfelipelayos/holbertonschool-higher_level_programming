def print_square(size):
    """print square with '#'

    Arguments:
        size {int} -- size of the square
    """

    if type(size) not in [int]:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) in [float] and size < 0:
        raise TypeError('size must be an integer')

    for i in range(size):
        for x in range(size):
            print('#', end="")
        print("")
