import unittest
from unittest.mock import Mock, patch

from maze import Maze
from shapes import Cell, Line, Point
from window import Window


class TestPoint(unittest.TestCase):
    def test_point_creation(self):
        p1 = Point(10, 20)
        self.assertEqual((p1.x, p1.y), (10, 20))


class TestLine(unittest.TestCase):
    def test_line_creation(self):
        p1 = Point(5, 5)
        p2 = Point(50, 50)
        line = Line(p1, p2)
        self.assertEqual((line.a, line.b), (p1, p2))


class TestCell(unittest.TestCase):
    def setUp(self):
        self.mock_window = Mock(spec=Window)
        self.p1 = Point(10, 10)
        self.p2 = Point(50, 50)

    def test_cell_creation(self):
        coords = (self.p1, self.p2)
        cell = Cell(coordinates=coords, window=self.mock_window, visited=True)
        self.assertEqual(cell.coordinates, coords)
        self.assertEqual(cell.walls, [True, True, True, True])
        self.assertTrue(cell.visited)
        self.assertEqual(cell._win, self.mock_window)

    def test_cell_calculate_center(self):
        cell = Cell(coordinates=(self.p1, self.p2), window=self.mock_window)
        center = cell._calculate_center()
        expected_center_x = 10 + (50 - 10) // 2  # p1.x + width // 2
        expected_center_y = 10 + (50 - 10) // 2  # p1.y + height // 2
        self.assertEqual(center.x, expected_center_x)
        self.assertEqual(center.y, expected_center_y)


class TestMaze(unittest.TestCase):
    # patch replace Window and sleep for all test in this class
    # This prevents actual GUI windows
    @patch("maze.Window", autospec=True)  # Mock the Window class
    @patch("maze.sleep", return_value=None)  # Mock sleep to avoid delays
    def setUp(self, mock_sleep, mock_window_class):
        self.mock_window_instance = mock_window_class.return_value

        self.num_rows = 5
        self.num_cols = 8

        self.maze = Maze(
            x1=10,
            y1=10,
            num_rows=self.num_rows,
            num_cols=self.num_cols,
            cell_size_x=20,
            cell_size_y=20,
            win=self.mock_window_instance,
            animation_delay=0,
            seed=42,
        )

    def test_maze_creation_dimensions(self):
        # Check if the grid of cells is created correctly
        self.assertEqual(len(self.maze._cells), self.num_rows)
        self.assertEqual(len(self.maze._cells[0]), self.num_cols)
        self.assertIsInstance(self.maze._cells[0][0], Cell)

    def test_break_entrance_and_exit(self):
        # Check top wall from first cell was removed
        self.assertFalse(self.maze._cells[0][0].walls[1])
        # Check if bottom wall from last cell was removed
        self.assertFalse(self.maze._cells[-1][-1].walls[3])

    def test_reset_cells_visited(self):
        # set some cells as visited
        self.maze._cells[0][0].visited = True
        self.maze._cells[1][1].visited = True

        self.maze._reset_cells_visited()
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.assertFalse(self.maze._cells[i][j].visited)


if __name__ == "__main__":
    unittest.main()
