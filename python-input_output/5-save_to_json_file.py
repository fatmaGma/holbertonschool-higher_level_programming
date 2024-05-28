#!/usr/bin/python3
"""module for JSON file writing operations"""

import json

def save_to_json_file(my_obj, filename):
    """
    write an obj to a txt file using JSON representation

    Args:
    my_obj: the obj to be serialized and written to the file 
    filename (str): the name of the file to write the JSON data to
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
