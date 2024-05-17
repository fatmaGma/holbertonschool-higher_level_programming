#!/usr/bin/python3
"""
defines a square with a private instance attribute: size
"""


class Square:
    """
    define attribute of square
    """
    def __init__(self, size=0):
        """
        initialize a square
        Args:
        size (int, optional): _description_. Defaults to 0.
        Raises:
        TypeError: size must be an integer
        ValueError: size must be >=0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns:
        int: the current area of the square.
        """
        return self.__size ** 2
