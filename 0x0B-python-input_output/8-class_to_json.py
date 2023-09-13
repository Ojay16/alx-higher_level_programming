#!/usr/bin/python3
"""Defines a python class to JSON function."""


def class_to_json(obj):
    """Returns a dictionary rep of a simple data struct."""
    return obj.__dict__
