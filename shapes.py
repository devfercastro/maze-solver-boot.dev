from tkinter import Canvas

from typing_extensions import Literal


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
