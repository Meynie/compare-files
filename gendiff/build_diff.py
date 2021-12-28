import os

from gendiff.parser_input import parser


def read_file(file_name):
    """Read file and return dictionary."""
    with open(file_name, 'r', encoding='utf-8') as file_object:
        file_type = os.path.splitext(file_name)[-1]
        file_data = file_object.read()
        return parser(file_data, file_type)


def generate_diff(file1, file2):
    """Find differences in files."""
    before_dict, after_dict = read_file(file1), read_file(file2)
    common = sorted(before_dict.keys() & after_dict.keys())
    before = sorted(before_dict.keys() - after_dict.keys())
    after = sorted(after_dict.keys() - before_dict.keys())
    diff = ['{']
    for key in before:
        diff.append(' - ' + key + ': ' + str(before_dict[key]))
    for key in common:
        if before_dict[key] == after_dict[key]:
            diff.append('   ' + key + ': ' + str(before_dict[key]))
        else:
            diff.append(' - ' + key + ': ' + str(before_dict[key]))
            diff.append(' + ' + key + ': ' + str(after_dict[key]))
    for key in after:
        diff.append(' + ' + key + ': ' + str(after_dict[key]))
    diff.append('}')
    result_diff = ''
    for elem in diff:
        result_diff = result_diff + elem + '\n'
    return result_diff
