def add_integer(a, b=98):
    """add two integers"""

    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')

    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    a = int(a)
    b = int(b)

    return a + b

def test_add_integer():
    assert add_integer(1,3.5) == 4
