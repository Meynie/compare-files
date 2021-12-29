# -*- coding: utf-8 -*-

"""Render JSON format"""

import json


def render(diff):
    return json.dumps(diff, indent=2)
