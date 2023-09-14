#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Reps a student."""

    def __init__(self, first_name, last_name, age):
        """Initializez a new Student.

        Args:
            first_name (str): First name of student.
            last_name (str): Last name of student.
            age (int): Age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary rep of Student.

        If attrs is a list of strings, reps only those attributes
        included in the list.

        Args:
            attrs (list): Attributes to rep.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of Student.
        Args:
            json (dict): key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
