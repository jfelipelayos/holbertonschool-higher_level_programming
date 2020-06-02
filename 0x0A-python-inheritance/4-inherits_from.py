#!/usr/bin/python3
def inherits_from(obj, a_class):

    status = issubclass(type(obj), a_class)
    return status
