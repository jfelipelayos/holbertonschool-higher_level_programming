#!/usr/bin/python3
"""Locked class
    """


class LockedClass:
    """Class to lock the creation of attributes
    exept if the name of the attribute its first_name
    """
    __slots__ = 'first_name'
