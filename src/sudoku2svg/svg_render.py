import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
from .sudoku_grid import SudokuGrid
from .viewable_sudoku_grid import ViewableSudokuGrid


package_directory = os.path.dirname(os.path.abspath(__file__))
template_directory = os.path.join(package_directory, "templates")

def sudoku2svg(sudoku: SudokuGrid):
    viewable_sudoku = ViewableSudokuGrid(sudoku)
    env = Environment(
        loader=FileSystemLoader(template_directory),
        autoescape=select_autoescape()
    )
    template = env.get_template("sudoku-grid.svg.jinja")
    cssCode = ''
    with open(os.path.join(template_directory, 'sudoku-grid.css'), 'r') as f:
        cssCode = f.read()
    svgStr = template.render(sudoku=viewable_sudoku, cssCode=cssCode)
    return svgStr.encode()