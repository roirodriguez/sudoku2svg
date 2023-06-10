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
    

class ViewableSudokuGrid(SudokuGrid):
    # copy constructor
    def __init__(self, sudoku: SudokuGrid):
        super().__init__(dimension=sudoku.dimension)
        for i, cell in enumerate(sudoku.cells):
            viewable_cell = ViewableSudokuCell(
                self,
                i, 
                value=cell.value, 
                isgiven=cell.isgiven, 
                corner_marks=cell.corner_marks, 
                center_marks=cell.center_marks, 
                bgcolor=cell.bgcolor
            )
            self._cells.append(viewable_cell)

    @property
    def svg_vieport_size(self):
        return 100 * (self.max_digit + 1)
    
    @property
    def svg_grid_size(self):
        return 100 * self.max_digit
    
    def svg_grid_to_viewport(self, x):
        return 100*x+50



class ViewableCornerMark(SvgRelativeGridPosition):
    def __init__(self, x: int, y: int, value: int):
        super().__init__(x, y)
        self._value = value

    @property
    def value(self):
        return self._value
    

class ViewableSudokuCell(SudokuCell):
    def __init__(
            self, sudoku: ViewableSudokuGrid,
            position, 
            value=None, 
            isgiven=False, 
            corner_marks:List[str] = [], 
            center_marks: List[str] = [], 
            bgcolor=1
        ):
        super().__init__(sudoku, position, value=value, isgiven=isgiven, corner_marks=corner_marks, 
                         center_marks=center_marks, bgcolor=bgcolor)
        self._row = position // self._max_digit + 1
        self._col = position % self._max_digit + 1
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
        ret = []
        n_marks = len(self._corner_marks)
        mark_positions = self._get_mark_positions(n_marks)
        for i, value in enumerate(self._corner_marks):
            x, y = mark_positions[i]
            ret.append(ViewableCornerMark(x, y, value))
        return ret
    
    def _get_mark_positions(self, n_marks):
        # svg positions sorted by fill order
        mark_positions = [(15, 27), (85, 27), (15, 91), (85, 91), (50, 27), (50, 91), (15, 59), (50, 59), (85, 59)]
        # remaining svg positions sorted by mark
        mark_positions = sorted(mark_positions[:len(self._corner_marks)], key=lambda x: x[1]*10+x[0])
        # fix case with 8 digits in, leave center blank
        if(n_marks == 8):
            mark_positions = self._get_mark_positions(7)
            mark_positions = mark_positions[:4] + [(85, 59)] + mark_positions[5:]
        return mark_positions

