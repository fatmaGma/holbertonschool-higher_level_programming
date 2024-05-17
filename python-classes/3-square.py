#!/usr/bin/python3
class Square:
    """
    Square class defines a square with a private instance attribute: size
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class with an optional size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns the current area of the square.
        """
        return self.__size ** 2
