#!/usr/bin/python3
"""module for file appending operations"""


def append_write(filename="", text=""):
    """
    Append a str to the end of a txt file and retrun the number of char added

    Args:
    filename (str): the path of the file to be written
    text (str): the text to be appended to the file

    Returns:
    int: the number of char added
    """
    with open(filename, 'a') as file:
            return file.write(text)
