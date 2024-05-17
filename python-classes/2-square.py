#!/usr/bin/python3
"""
define a class
"""
class Square:
    def __init__(self, size=0):
        """
        Initializes a new square
        Args:
        size (int): size of a new square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
