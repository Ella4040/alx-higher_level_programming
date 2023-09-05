#!/usr/bin/python3
"""define a class rectangle"""


class Rectangle:
    """represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the attributes
        Args:
            width(int) is 0 if not set
            height(int) is 0 if not set
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """get the value of width"""

        return self.__width

    @width.setter
    def width(self, value):
        """elemnts the width
        Args: width(int)"""

        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the value of height"""

        return self.__height

    @height.setter
    def height(self, value):
        """elements of height
        Args: width(int)"""

        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """define the area of the rectangle"""

        return (self.__height * self.__width)

    def perimeter(self):
        """define  perimeter of rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """returns rectangle"""

        if self.__width == 0 or self.height == 0:
            return ""
        else:
            rectangle_str = ""
            for i in range(self.height):
                rectangle_str += (self.width * "#") + "\n"
            return rectangle_str[:-1]
