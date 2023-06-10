import re
from typing import List


_VALID_DIMENSIONS = [2, 3]


def _sudoku_size(dimension:int=3):
    if not dimension:
        raise ValueError
    return dimension * dimension * dimension * dimension


def _sudoku_max_digit(dimension:int=3):
    if not dimension:
        raise ValueError
    return dimension * dimension

def _sudoku_size_dim(size:int=81):
    valid = { _sudoku_size(v): v for v in _VALID_DIMENSIONS }
    if not size in valid:
        raise ValueError
    return valid[size]


class SudokuGrid:
    def __init__(self, dimension:int=3):
        if not dimension in _VALID_DIMENSIONS:
            raise ValueError
        self._cells = []
        self._dimension = dimension

    @property
    def cells(self):
        return self._cells
    
    @property
    def dimension(self):
        return self._dimension
    
    @property
    def max_digit(self):
        return _sudoku_max_digit(self.dimension)
    

class SudokuCell:
    def __init__(self, sudoku: SudokuGrid, position: int, value: int=None, isgiven: bool=False, 
                 corner_marks:List[int] = [], 
                 center_marks:List[int] =[], 
                 bgcolor=1):
        self._max_digit = _sudoku_max_digit(sudoku.dimension)
        if position and not 0 <= position < _sudoku_size(sudoku.dimension):
            raise ValueError    
        if value and not 0 < value <= self._max_digit:
            raise ValueError
        self._position = position
        self._corner_marks = corner_marks
        self._center_marks = center_marks
        self._value = value
        self._isgiven = isgiven
        self._bgcolor = bgcolor
    
    @property
    def corner_marks(self):
        # return copy
        return list(self._corner_marks)
    
    @corner_marks.setter
    def corner_marks(self, marks: List[int]):
        self._corner_marks = sorted(marks)
    
    @property
    def center_marks(self):
        # return copy
        return list(self._center_marks)
    
    @center_marks.setter
    def center_marks(self, marks: List[int]):
        self._center_marks = sorted(marks)

    # getter without a setter is readonly in python
    @property
    def position(self):
        return self._position

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value: int):
        if value > self._max_digit:
            raise ValueError
        self._value = value

    @property
    def isgiven(self):
        return self._isgiven
    
    @property
    def bgcolor(self):
        return self._bgcolor
    
    @bgcolor.setter
    def bgcolor(self, color_code: int):
        self._bgcolor = color_code


class SudokuBuilder:
    @staticmethod
    def fromString(puzzleStr: str):
        size = len(puzzleStr)
        dim = _sudoku_size_dim(size)
        max_digit = _sudoku_max_digit(dim)
        sudoku = SudokuGrid(dim)
        valid_regex = re.compile(f"^[0-{max_digit}]{{{size}}}$")
        if valid_regex.match(puzzleStr):
            for i in range(size):
                value = int(puzzleStr[i])
                if value == 0:
                    cell = SudokuCell(sudoku, i)
                else:
                    cell = SudokuCell(sudoku, i, value=value, isgiven=True)
                sudoku.cells.append(cell)
        return sudoku
    
    @staticmethod
    def emptyGrid(dimension:int=3):
        sudoku = SudokuGrid(dimension)
        for i in range(_sudoku_size(dimension)):
            cell = SudokuCell(sudoku, i)
            sudoku.cells.append(cell)
        return sudoku