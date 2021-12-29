from gendiff import format


def get_formatter(name_format):
    formats = {
        'string': format.string,
        'plain': format.plain,
        'json': format.json
    }
    return formats[name_format]
