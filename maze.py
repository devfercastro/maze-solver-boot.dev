from time import sleep

from shapes import Cell, Point
from window import Window


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window,
        animation_delay=0.05,
    ):
        """
        Boot.dev: Create a class that holds all the cells in the maze in a 2-dimensional grid, a list of list.
        Initialize data members for all inputs then call `_create_cells()`.
        """
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.animation_delay = animation_delay

        self._cells: list[list[Cell]] = []

        self._create_cells()

    def _create_cells(self):
        """
        Boot.dev: This method should fill a `self._cells` list with list of cells. Each top-level list is a column of `Cell` objects. Once the matrix is populated it should call its `_draw_cell()` method on each `Cell`.
        """
        # Populate the maze
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                row.append(Cell(window=self.win))
            self._cells.append(row)

        # Draw each cell
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)
                self._animate()

    def _draw_cell(self, i, j):
        """
        Boot.dev: This method should calculate the x/y position of the `Cell` based on `i`, `j`, the `cell_size`, and the x/y position of the Maze itself. The x/y position of the maze represents how many pixels from the top and left the maze should start from the side of the window.
        Once that's calculated, it should draw the cell and call the maze's `_animate()` method.
        """
        # Get the specific cell
        cell = self._cells[i][j]  # i = coordinate y, j = coordinate x

        # Calculate the starting cell coordinates
        cell_start_x = self.x1 + (j * self.cell_size_x)
        cell_start_y = self.y1 + (i * self.cell_size_y)

        start_point = Point(
            cell_start_x, cell_start_y
        )  # for start point starting cell coordinates are used alone
        end_point = Point(
            cell_start_x + self.cell_size_x,
            cell_start_y
            + self.cell_size_y,  # for ending point I need to add the x and y cell's sizes
        )

        # setup coordinates
        cell.coordinates = (start_point, end_point)

        # draw it
        cell.draw()

    def _animate(self):
        """
        The animate method is what allows us to visualize what the algorithms are doing in real time. It should simply call the window's `redraw()` method, then use time.sleep() for a short amount of time so you eyes keep up with each render frame. I slept for `0.05` seconds.
        """
        self.win.redraw()
        sleep(self.animation_delay)
