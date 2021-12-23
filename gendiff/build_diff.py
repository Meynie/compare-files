import json


def generate_diff(file1, file2):
    """Find differences in files."""
    file1 = json.load(open(file1))
    file2 = json.load(open(file2))
    common = sorted(file1.keys() & file2.keys())
    before = sorted(file1.keys() - file2.keys())
    after = sorted(file2.keys() - file1.keys())
    result = '{' + '\n'
    for i in before:
        result = result + ' - ' + i + ': ' + str(file1[i]) + '\n'
    for i in common:
        if file1[i] == file2[i]:
            result = result + '   ' + i + ': ' + str(file1[i]) + '\n'
        else:
            result = result + ' - ' + i + ': ' + str(file1[i]) + '\n'
            result = result + ' + ' + i + ': ' + str(file2[i]) + '\n'
    for i in after:
        result = result + ' + ' + i + ': ' + str(file2[i]) + '\n'
        result = result + '}'
        return result
