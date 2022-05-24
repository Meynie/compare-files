# Generate diff

### Tests and linter status:

[![linter-check](https://github.com/Meynie/python-project-lvl2/actions/workflows/github-actions.yml/badge.svg)](https://github.com/Meynie/python-project-lvl2/actions/workflows/github-actions.yml)
<a href="https://codeclimate.com/github/Meynie/python-project-lvl2/maintainability"><img src="https://api.codeclimate.com/v1/badges/69f4f7010a2715b95a39/maintainability" /></a>

## Description
Compares two files and shows the differences.

```
$ gendiff -h

usage: gendiff [-h] [-f FORMAT] first_file second_file

Generate diff.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```
## Feature:
- Supported formats: YAML, JSON
- Report generation as plain JSON, text, structured text 
- Can be used as CLI tool or external library

## Installation
```
$ pip install git+https://github.com/Meynie/python-project-lvl2.git
```
## Usage
```
gendiff -f plain (or string or json) first_file second_file
```
## Example

### First file
simple_before.json
```
{
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": false
}
```
### Second file
simple_after.json
```
{
  "timeout": 20,
  "verbose": true,
  "host": "hexlet.io"
}
```
### Result
```
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  + timeout: 20
  - timeout: 50
  + verbose: true
}
```
