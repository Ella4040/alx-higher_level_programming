#!/usr/bin/python3
"""This module has a function that checks if an object is an instance of a
class or of an inherited class
"""


def is_kind_of_class(obj, a_class):
    """Function returns True if the object is an instance
    """

    return True if isinstance(obj, a_class) else False
