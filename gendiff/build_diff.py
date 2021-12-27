import json


def read_file(file):
    res = json.load(open(file))
    return res


def generate_diff(file1, file2):
    """Find differences in files."""
    before_dict = read_file(file1)
    after_dict = read_file(file2)
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
