from tkinter import Canvas, Tk

from typing_extensions import Literal


class Window:
    # Windows class's constructor
    # 1. The constructor should take a `width` and `height`. This will be the size of the new window we create in pixels
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height
        # 2. It should create a new root widget using `TK()` and save it as a data member
        self.__root = Tk()
        # 3. Set the `title` property of the root widget
        self.__root.title = "Maze Solver"
        # 4. Create a `Canvas` widget and save it as a data member
        self.__canvas = Canvas(self.__root, width=width, height=height)
        # 5. Pack the canvas widget so that it's ready to be drawn
        self.__canvas.pack()
        # 6. Create a data member to represent that the window is "running", and set it to `False`
        self.__running = False

        # Connects `self.close()` method to the "delete window" action
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    # redraw() method
    def redraw(self):
        """
        This method simply calls the root widget's `update_idletasks()` and `update()` methods. Each time this is called, the window will redraw itself.
        """
        self.__root.update_idletasks()
        self.__root.update()

    # wait_for_close() method
    def wait_for_close(self):
        """
        This method sets `self.running` to `True`. Next, it calls `self.redraw()` over and over as long as the running state remains `True`
        """
        self.__running = True

        while self.__running:
            self.redraw()

    # the close() method
    def close(self):
        """
        This method simply sets `self.running` to `False`.
        """
        self.__running = False

    def draw_line(self, line, fill_color: Literal["black", "red"]):
        """
        It takes an instance of `Line` and a color as inputs, then calls the `Line`s `draw()` method.
        """
        line.draw(self.__canvas, fill_color)
