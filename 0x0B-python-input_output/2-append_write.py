#!/usr/bin/python3
"""Defines a file-appending function."""

def append_write(filename="", text=""):
    """Appends string to d end of a UTF8 text file.
    Args:
        filename (str): Name of  file to append to.
        text (str): String to append to file.
    Returns:
         Num of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
