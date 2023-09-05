#!/usr/bin/python3
"""create a class rectangle"""


class Rectangle:
    """define an object class"""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle
        Args:
            width(int)
            height(int)
        """

        self.width = width
        self.height = height

    @property
    def height(self):
        """define the height"""

        return (self.__height)

    @height.setter
    def height(self, value):
        """Args: height(int)"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """define the width"""

        return (self.__width)

    @width.setter
    def width(self, value):
        """ Args: width(int)"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
