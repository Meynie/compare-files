import json

import yaml


def parser(file_data, file_type):
    """Parse input data into appropriate format."""
    mapping = {
        '.json': lambda file_data: json.loads(file_data),
        '.yaml': lambda file_data: yaml.load(file_data, Loader=yaml.SafeLoader),
    }
    return mapping[file_type](file_data)
