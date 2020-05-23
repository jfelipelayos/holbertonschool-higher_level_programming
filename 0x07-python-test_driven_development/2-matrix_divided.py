#!/usr/bin/python3
"""
Divide matrix
"""


def matrix_divided(matrix, div):
    """Divide a matrix

    Arguments:
        matrix {list} -- matrix to divide
        div {int} -- number to divide

    Raises:
        TypeError: div must be a number
        TypeError: matrix must be a matrix (list of lists) '
                        'of integers/floats

    Returns:
        list -- new matrix divided
    """
    divided_matrix = []
    size = 0

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if matrix == [] or matrix == [[]]:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if not isinstance(matrix[0], list):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if len(matrix[0]) <= 0:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    for row in matrix:
        divided_row = []
        if type(row) is not list:
            raise TypeError('matrix must be a matrix (list of lists) '
                            'of integers/floats')
        if size is 0:
            size = len(row)
        elif len(row) is not size:
            raise TypeError('Each row of the matrix must have the same size')
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError('matrix must be a matrix (list of lists) '
                                'of integers/floats')
            if div is True or div is False:
                raise TypeError("div must be a number")
            divided_row.append(round(item / div, 2))
        divided_matrix.append(divided_row)
    return divided_matrix
