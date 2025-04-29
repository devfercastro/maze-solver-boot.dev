from shapes import Cell, Point
from window import Window

# windows dimentions
WIDTH, HEIGHT = 800, 600


def main():
    # create a window
    win = Window(WIDTH, HEIGHT)

    # draw some cells with black lines
    cell1 = Cell((Point(2, 2), Point(100, 100)), win)
    cell1.draw()
    cell2 = Cell((Point(2, 102), Point(100, 202)), win)
    cell2.draw()

    # wait for the window to close
    win.wait_for_close()


if __name__ == "__main__":
    main()
