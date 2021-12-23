import json


def generate_diff(file1, file2):
    """Find differences in files."""
    file1 = json.load(open(file1))
    file2 = json.load(open(file2))
    common = sorted(file1.keys() & file2.keys())
    before = sorted(file1.keys() - file2.keys())
    after = sorted(file2.keys() - file1.keys())
    diff = ['{']
    for key in common:
        if file1[key] == file2[key]:
            diff.append('   ' + key + str(file1[key]))
        else:
            diff.append(' - ' + key + ': ' + str(file1[key]))
            diff.append(' + ' + key + ': ' + str(file2[key]))
    for key in before:
        diff.append(' - ' + key + ': ' + str(file1[key]))
    for key in after:
        diff.append(' + ' + key + ' ' + str(file2[key]))
    diff.append('}')
    result_diff = ''
    for elem in diff:
        result_diff = result_diff + elem + '\n'
    return result_diff
