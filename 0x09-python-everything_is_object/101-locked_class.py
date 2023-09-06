#!/usr/bin/python3
"""
This is a module that containts a clas that avoids
dynmaically created attributes
"""

class LockedClass:
    """
    Secret class
    """

    def __setattr__(self, attr, value):
        """
        Method that allows the creation of first_name attribute but prevents
        the creation of any other instance attributes.
        """
        msg = "'LockedClass' object has no attribute"
        if attr == 'first_name':
            super().__setattr__(attr, value)
        else:
            raise AttributeError(msg+" '{}'".format(attr))
