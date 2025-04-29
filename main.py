from shapes import Line
from window import Window

# windows dimentions
WIDTH, HEIGHT = 800, 600


def main():
    # create a window
    win = Window(WIDTH, HEIGHT)

    # draw a black line
    line = Line()
    win.draw_line(line, "black")

    # wait for the window to close
    win.wait_for_close()


if __name__ == "__main__":
    main()
