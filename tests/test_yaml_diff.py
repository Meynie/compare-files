# -*- coding: utf-8 -*-

"""YAML files diff test."""

from gendiff.generate import generate_diff
from tests.expected import (
    SIMPLE_DIFF_STRING,
    COMPLEX_DIFF_STRING,
    SIMPLE_DIFF_JSON,
    COMPLEX_DIFF_JSON,
    SIMPLE_DIFF_PLAIN,
    COMPLEX_DIFF_PLAIN,
)

PATH_AFTER_SIMPLE = 'tests/fixture/simple_after.yaml'
PATH_BEFORE_SIMPLE = 'tests/fixture/simple_before.yaml'

PATH_AFTER_COMPLEX = 'tests/fixture/complex_after.yaml'
PATH_BEFORE_COMPLEX = 'tests/fixture/complex_before.yaml'


def test_simple_string_diff():
    difference = generate_diff(
        PATH_BEFORE_SIMPLE,
        PATH_AFTER_SIMPLE,
        'string')
    assert difference == SIMPLE_DIFF_STRING


def test_complex_string_diff():
    difference = generate_diff(
        PATH_BEFORE_COMPLEX,
        PATH_AFTER_COMPLEX,
        'string')
    assert difference == COMPLEX_DIFF_STRING


def test_simple_json_diff():
    difference = generate_diff(
        PATH_BEFORE_SIMPLE,
        PATH_AFTER_SIMPLE,
        'json')
    assert difference == SIMPLE_DIFF_JSON


def test_complex_json_diff():
    difference = generate_diff(
        PATH_BEFORE_COMPLEX,
        PATH_AFTER_COMPLEX,
        'json')
    assert difference == COMPLEX_DIFF_JSON


def test_simple_plain_diff():
    difference = generate_diff(
        PATH_BEFORE_SIMPLE,
        PATH_AFTER_SIMPLE,
        'plain')
    assert difference == SIMPLE_DIFF_PLAIN


def test_complex_plain_diff():
    difference = generate_diff(
        PATH_BEFORE_COMPLEX,
        PATH_AFTER_COMPLEX,
        'plain')
    assert difference == COMPLEX_DIFF_PLAIN
