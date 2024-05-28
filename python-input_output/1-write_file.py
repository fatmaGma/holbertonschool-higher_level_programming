#!/usr/bin/python3
"""module for file writing operations"""


def write_file(filename="", text=""):
    """
    write a string to a text file (UTF-8) and return the number of char written
    
    args:
    filemane (str): the path to the file to be written
    test (str): the text to be written to the file 

    Returns:
    it: the number of char written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
