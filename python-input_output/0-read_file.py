#!/usr/bin/python3
"""Module for file reading operations."""


def read_file(filename = ""):
    """read a file and print it .

    args:
    filename: file to read and print.
    """
    with open(filename, 'r', encoding = 'utf-8') as file:
        content = file.read()
        print(content, end='')
