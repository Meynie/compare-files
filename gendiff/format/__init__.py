# -*- coding: utf-8 -*-

"""Renders."""

from gendiff.format.json import render as json
from gendiff.format.plain import render as plain
from gendiff.format.string import render as string

__all__ = ['json', 'plain', 'string']
