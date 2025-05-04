import random
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
        # L10: Break Walls
        # Add another parameter to `Maze` caled `seed` that defaults to `None`
        seed=None,
    ):
        """
        Boot.dev: Create a class that holds all the cells in the maze in a 2-dimensional grid, a list of list.
        Initialize data members for all inputs then call `_create_cells()`.
        """
        # L10: Break Walls
        # Then, in your constructor, if the `seed` isn't none you call `random.seed(seed)`
        if seed:
            random.seed(seed)

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

        self._break_entrance_and_exit()

        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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

    def _draw_cell(self, i: int, j: int):
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

    def _break_entrance_and_exit(self):
        """
        Boot.dev: The entrance to the maze will always be at the top of the top-left cell, the exit always at the bottom of the bottom-right cell.
        Add a `_break_entrance_and_exit()` method that removes an outer wall from those cells, and calls `_draw_cell()` after each removal.
        Next, write another unit test to ensure it's working.
        """
        last_cell_j = self.num_cols - 1
        last_cell_i = self.num_rows - 1

        # Get the corresponding cells
        first_cell = self._cells[0][0]
        last_cell = self._cells[last_cell_i][last_cell_j]

        first_cell.walls[1] = False  # Set top first-cell's wall to false
        last_cell.walls[3] = False  # Set bottom last-cell's wall to false

        # Draw cells
        self._draw_cell(0, 0)
        self._draw_cell(last_cell_i, last_cell_j)

    def _break_walls_r(self, i: int, j: int):
        """
        L10: Break Walls
        The recursive `_break_walls_r(self, i, j)` method is a depth-first traversal through the cells, breaking down walls as it goes. I'lle describe the algorithm I used, but feel free to write your own from scratch if your're up to it!
        """
        # 1. Mark the current cell as visited
        self._cells[i][j].visited = True
        # 2. In an infinite loop:
        while True:
            # 2.1. Create a new empty list to hold the `i` and `j` values you will need to visit
            to_visit = []
            # 2.2. Check the cells that are directly adjacent to the current cell. Keep track of any that have not been visited as "possible directions" to move to
            if i > 0 and not self._cells[i - 1][j].visited:  # Top cell
                to_visit.append((i - 1, j))
            if i < self.num_rows - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if j < self.num_cols - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            # 2.3. If there are zero directions you can go from the current cell, then draw the current cell and `return` to break out of the loop
            if not to_visit:
                self._draw_cell(i, j)
                return
            # 2.4. Otherwise, pick a random direction
            next_i, next_j = random.choice(to_visit)
            # 2.5. Knock down the walls between the current cell and the chosen cell
            if next_j == j - 1:  # Moving to left
                self._cells[i][j].walls[0] = False  # Remove current cell's left wall
                self._cells[i][j - 1].walls[2] = False  # And left neighbor's right wall
            elif next_j == j + 1:  # Moving to right
                self._cells[i][j].walls[2] = False  # Remove current cell's right wall
                self._cells[i][j + 1].walls[0] = False  # And right neighbor's left wall
            elif next_i == i - 1:  # Moving up
                self._cells[i][j].walls[1] = False  # Remove current cell's top wall
                self._cells[i - 1][j].walls[3] = False  # And top neighbor's bottom wall
            elif next_i == i + 1:  # Moving down
                self._cells[i][j].walls[3] = False  # Remove current cell's bottom wall
                self._cells[i + 1][j].walls[1] = False  # And bottom neighbor's top wall
            # 2.6. Move to the chosen cell by recursively calling `_break_walls_r`
            self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
        # L11: Reset the Cell's 'visited' Property
        # Write `_reset_cells_visited` method. It should reset the `visited` property of all the cells in the `Maze` to false. Call it after `_break_walls_r` so we can reuse the `visited` property when solving the maze in the next step.
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j].visited = False
