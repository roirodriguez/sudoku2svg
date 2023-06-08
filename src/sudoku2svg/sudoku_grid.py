import re
from typing import List

class SudokuCell:
    def __init__(self, position: int, value: int=None, isgiven: bool=False, 
                 corner_marks:List[int] = [], 
                 center_marks:List[int] =[], 
                 bgcolor=1):
        if position and not 0 <= position < 16:
            raise ValueError    
        if value and not 0 <= value < 16:
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
        if value > 4:
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
    

class SudokuGrid:
    def __init__(self):
        self._cells = []

    @property
    def cells(self):
        return self._cells


class SudokuBuilder:
    @staticmethod
    def fromString(puzzleStr: str):
        sudoku = SudokuGrid()
        valid_regex = re.compile("^[0-4]{16,16}$")
        if valid_regex.match(puzzleStr):
            for i in range(16):
                value = int(puzzleStr[i])
                if value == 0:
                    cell = SudokuCell(i)
                else:
                    cell = SudokuCell(i, value=value, isgiven=True)
                sudoku.cells.append(cell)
        return sudoku
    
    @staticmethod
    def emptyGrid():
        sudoku = SudokuGrid()
        for i in range(16):
            cell = SudokuCell(i)
            sudoku.cells.append(cell)
        return sudoku