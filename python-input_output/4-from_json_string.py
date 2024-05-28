#!/usr/bin/python3
"""module for JSON deserialization operations"""

import json

def from_json_string(my_str):
    """
    return an obj (python data structure) represented by a JSON

    Args:
    my_str (str): the JSON str to be deserialized

    Returns:
    object: the python object represented by the JSON string
    """
    return json.loads(my_str)
