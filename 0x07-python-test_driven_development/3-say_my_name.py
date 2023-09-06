#!/usr/bin/python3
"""function that takes in two arguments and prints out a statement that contains the argments
"""


def say_my_name(first_name, last_name=""):
    """prints out a statement with the two argments
    Args:
        first_name: the first string
        last_name: the second string
    Return:
        Nothing
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
