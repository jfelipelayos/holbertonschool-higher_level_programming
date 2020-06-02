#!/usr/bin/python3
"""[summary]
    """


class MyInt(int):
    """My int class

    Arguments:
        int {int} -- Int inherence
    """

    def __eq__(self, other):

        return super().__ne__(other)

    def __ne__(self, other):

        return super().__eq__(other)
