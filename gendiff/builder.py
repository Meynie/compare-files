from gendiff.constants import ADDED, DELETED, CHANGED, NESTED, UNCHANGED


def builder(before, after):
    """Build structure report."""
    keys = list(before.keys() | after.keys())
    return {
        key: generate_node(key, before, after)
        for key in sorted(keys)
    }


def generate_node(key, before, after):
    """Generate tree nodes."""
    after_value = after.get(key)
    before_value = before.get(key)
    if before_value is None:
        node = {
            'type': ADDED,
            'value': get_type_value(after_value),
        }
    elif after_value is None:
        node = {
            'type': DELETED,
            'value': get_type_value(before_value),
        }
    elif isinstance(before_value, dict) and isinstance(after_value, dict):
        node = {
            'type': NESTED,
            'value': builder(before_value, after_value),
        }
    elif before_value == after_value:
        node = {
            'type': UNCHANGED,
            'value': get_type_value(before_value),
        }
    elif before_value != after_value:
        node = {
            'type': CHANGED,
            'old_value': get_type_value(before_value),
            'new_value': get_type_value(after_value),
        }
    return node


def get_type_value(elem_value):
    """Edit value type."""
    if elem_value is True:
        return 'true'
    if elem_value is False:
        return 'false'
    return elem_value
