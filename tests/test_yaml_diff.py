# -*- coding: utf-8 -*-

"""YAML files diff test."""

from gendiff.build_diff import generate_diff
from tests.expected import DIFFERENCE_STRING


def test_generate_diff():
    """Test generate_diff."""
    actual = generate_diff('./tests/fixtures/before.yaml',
                           './tests/fixtures/after.yaml')
    assert actual == DIFFERENCE_STRING
