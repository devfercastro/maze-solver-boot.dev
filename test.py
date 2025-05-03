import unittest

from maze import Maze
from window import Window


class Tests(unittest.TestCase):
    def_win = Window(800, 600)
    def_maze = Maze(0, 0, 5, 5, 10, 10, def_win, 0)

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


if __name__ == "__main__":
    unittest.main()
