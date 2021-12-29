# -*- coding: utf-8 -*-

import os

from gendiff.parser_input import parser
from gendiff.builder import builder
from gendiff.format.get_format import get_formatter


def read_file(file_name):
    """Open and read file."""
    with open(file_name, 'r', encoding='utf-8') as file_object:
        file_type = os.path.splitext(file_name)[-1]
        file_data = file_object.read()
        return parser(file_data, file_type)


def generate_diff(file1, file2, output='string'):
    """Find differences in files."""
    before_dict, after_dict = read_file(file1), read_file(file2)
    diff = builder(before_dict, after_dict)
    return get_formatter(output)(diff)
