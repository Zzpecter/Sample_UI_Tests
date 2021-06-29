"""
Python helper module for reading the contents of different file formats.


Functions:

    read_json(file) -> dict

Misc variables:
    file
"""
import json


def read_json(file):
    """
    Helper function for reading JSON files
    Args:
        file(str): Path to the file to be read

    Returns:
        data(dict): Dict-parsed data of the JSON file read
    """
    with open(file) as file_stream:
        data = json.load(file_stream)
    return data

