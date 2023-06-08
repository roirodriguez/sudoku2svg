from typing import List
from .sudoku_grid import SudokuCell, SudokuGrid

class SvgRelativeGridPosition:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    

class ViewableCornerMark(SvgRelativeGridPosition):
    def __init__(self, x: int, y: int, value: int):
        super().__init__(x, y)
        self._value = value

    @property
    def value(self):
        return self._value


class ViewableSudokuCell(SudokuCell):
    def __init__(self, position, value=None, isgiven=False, corner_marks:List[str] = [], center_marks: List[str] = [], bgcolor=1):
        super().__init__(position, value=value, isgiven=isgiven, corner_marks=corner_marks, 
                         center_marks=center_marks, bgcolor=bgcolor)
        self._row = position // 4 + 1
        self._col = position % 4 + 1
        # svg position relative to parent (full svg in this case, 50px margin and 100px / cell in viewport)
        self._svg_position = SvgRelativeGridPosition(50 + 100 * (self._col - 1), 50 + 100 * (self._row - 1))

    @property
    def row(self):
        return self._row
    
    @property
    def col(self):
        return self._col
    
    @property
    def svg_position(self):
        return self._svg_position
    
    @property
    def corner_marks(self):
        # returns a list of ViewableCornerMark objects
        mark_positions = [(15, 27), (85, 27), (15, 91), (85, 91)]
        ret = []
        for i, value in enumerate(self._corner_marks):
            x, y = mark_positions[i]
            ret.append(ViewableCornerMark(x, y, value))
        return ret


class ViewableSudokuGrid(SudokuGrid):
    # copy constructor
    def __init__(self, sudoku: SudokuGrid):
        super().__init__()
        for i, cell in enumerate(sudoku.cells):
            viewable_cell = ViewableSudokuCell(
                i, 
                value=cell.value, 
                isgiven=cell.isgiven, 
                corner_marks=cell.corner_marks, 
                center_marks=cell.center_marks, 
                bgcolor=cell.bgcolor
            )
            self._cells.append(viewable_cell)