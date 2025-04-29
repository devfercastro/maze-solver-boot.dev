from tkinter import Canvas

from typing_extensions import Literal

from window import Window


class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        # It should simply store 2 public data members:
        # x - the x-coordinate (horizontal) in pixels of the point.
        self.x = x  # x = 0 is the left of the screen.
        # y - the y-coordinate (vertical) in pixels of the point.
        self.y = y  # y = 0 is the top of the screen.

    def __repr__(self) -> str:
        return f"P({self.x}, {self.y})"


class Line:
    def __init__(self, a: Point = Point(0, 2), b: Point = Point(100, 2)) -> None:
        print(a, b)
        # Takes 2 points as input, and saves them as data members.
        self.a = a
        self.b = b

    def draw(self, canvas: Canvas, fill_color: Literal["black", "red"]):
        """
        Takes a canvas and a fill color as input. The color will just be a string like "black" or "red", then it will call the canva's `create_line()` method.
        """
        canvas.create_line(
            self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_color, width=2
        )


class Cell:
    def __init__(
        self,
        coordinates: tuple[Point, Point] = (Point(0, 0), Point(10, 10)),
        window: Window = None,
    ):
        if window is None:
            raise Exception("Cell instance must have a declared 'Window' instance")

        # It should know which walls it has, know where it exists on the canvas in x/y coordinates and have access to the window so that it can draw itself
        self.walls = (True, True, True, True)  # Order left, top, right, bottom
        self.coordinates = coordinates
        self._win = window

    def draw(self):
        # It takes the x/y coordinates of its top-left corner, and its bottom-right corner as input.
        top_left_corner, bottom_right_corner = self.coordinates

        wall_points = [
            (
                Point(top_left_corner.x, top_left_corner.y),
                Point(top_left_corner.x, bottom_right_corner.y),
            ),  # Left wall line points
            (
                Point(top_left_corner.x, top_left_corner.y),
                Point(bottom_right_corner.x, top_left_corner.y),
            ),  # Top wall line points
            (
                Point(bottom_right_corner.x, top_left_corner.y),
                Point(bottom_right_corner.x, bottom_right_corner.y),
            ),  # Right wall line points
            (
                Point(top_left_corner.x, bottom_right_corner.y),
                Point(bottom_right_corner.x, bottom_right_corner.y),
            ),  # Bottom wall line points
        ]

        for i, points in enumerate(wall_points):
            # If the current wall is true, use their corresponding points to draw a trace a line
            if self.walls[i]:
                current_line = Line(*points)
                self._win.draw_line(current_line, "black")
