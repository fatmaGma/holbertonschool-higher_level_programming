#!/usr/bin/python3
"""Module for JSON file reading operations."""

import json

def load_from_json_file(filename):
    """
    Create an object from a "JSON file".

    Args:
    filename (str): The name of the file to read the JSON data from.

    Returns:
    object: The Python object represented by the JSON data.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

