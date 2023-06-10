# README

## Description

Small library to get a svg representation of a sudoku grid, with corner / center mark and coloring support.

Intended as a toy project and python template for small projects, covering basic python packaging and testing.

SVG template and CSS code borrowed from https://github.com/grantm/sudoku-web-app.

## Installation

```bash
$ python setup.py install
```

## Usage

Example usage in Jupyter Notebook: [usage_example.ipynb](doc/usage_example.ipynb)

Didn't manage to get github show inline svg in that jupyter notebook, so here's a sample output:

![Sample output](doc/sample_output.png)

## TODO

- pylint this
- add support for testing
- cleanup css
- migrate to pypa?
- allow SudokuGrid to work with friendly coordinates (row, col) just as ViewableSudokuGrid does.
- input validation in corner / center marks

## Licence

MIT. See [LICENCE](LICENCE) file.