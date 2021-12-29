# -*- coding: utf-8 -*-

"""Render plain format"""

from gendiff.constants import (
    ADDED,
    DELETED,
    CHANGED,
    NESTED,
    UNCHANGED,
    COMPLEX
)


def render(diff, parent=''):
    if not isinstance(diff, dict):
        return str(diff)

    result_array = []
    entry = ''

    for node_key, node_value in diff.items():
        prop = get_property(parent, node_key)
        node_type = node_value.get('type')

        if node_type == ADDED:
            entry = "Property '{0}' was added with value: '{1}'".format(
                prop,
                get_value(node_value),
            )
        elif node_type == DELETED:
            entry = "Property '{0}' was removed".format(prop)

        if node_type == NESTED:
            entry = render(node_value.get('value'), prop)
        elif node_type == CHANGED:
            entry = "Property '{0}' was changed. From '{1}' to '{2}'".format(
                prop,
                node_value.get('old_value'),
                node_value.get('new_value'),
            )
        elif node_type == UNCHANGED:
            continue

        result_array.append(entry)
    return '\n'.join(result_array)


def get_value(node):
    """Return node value."""
    node_value = node.get('value')
    if isinstance(node_value, dict):
        return COMPLEX
    return str(node_value)


def get_property(parent, prop_name):
    """Return property value."""
    if not parent:
        return prop_name
    return '{parent}.{prop}'.format(parent=parent, prop=prop_name)
