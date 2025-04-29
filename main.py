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
    cell2 = Cell((Point(2, 202), Point(100, 302)), win)
    cell2.draw()

    cell3 = Cell((Point(202, 202), Point(300, 302)), win)
    cell3.draw()

    # draw connecting lines
    cell1.draw_move(cell2, True)
    cell2.draw_move(cell3, False)
    cell3.draw_move(cell1, True)

    # wait for the window to close
    win.wait_for_close()


if __name__ == "__main__":
    main()
