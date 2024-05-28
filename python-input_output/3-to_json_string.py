#!/usr/bin/python3
"""module for JSON serialization operation"""

import json

def to_json_string(my_obj):
    """
    Return the JSON representation of an obj (str)

    Args:
    my_obj: the obj to be serialized to JSON

    Returns:
    str: the JSON representation of the obj
    """
    return json.dumps(my_obj)
