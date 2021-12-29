#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from gendiff.generate import generate_diff


def main():
    """Outputs differences between two files."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        action='store',
        help='set format of output',
    )
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
