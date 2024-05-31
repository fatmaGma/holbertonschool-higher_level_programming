#!/usr/bin/python3
"""define a class student"""


class Student:
    """Define a student"""

    def __init__(self, first_name, last_name, age):
    """
    args:
    first_name, last_name, et  age
    """
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            filtered_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_dict[attr] = getattr(self, attr)
            return filtered_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
