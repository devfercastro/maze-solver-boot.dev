import unittest

from maze import Maze
from window import Window


# TODO: This test sucks, improve its quality
class Tests(unittest.TestCase):
    def_win = Window(800, 600)
    num_rows = 5
    num_cols = 5
    seed = 1
    def_maze = Maze(0, 0, num_rows, num_cols, 10, 10, def_win, 0, seed)

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, self.def_win, 0)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_break_entrances_and_exit(self):
        self.assertFalse(self.def_maze._cells[0][0].walls[1])
        self.assertFalse(self.def_maze._cells[-1][-1].walls[3])

    def test_reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.assertFalse(self.def_maze._cells[i][j].visited)


if __name__ == "__main__":
    unittest.main()
