from maze import Maze
from window import Window

# windows dimentions
WIDTH, HEIGHT = 1366, 768


def main():
    # create a window
    win = Window(WIDTH, HEIGHT)

    # draw a maze
    maze = Maze(
        WIDTH // 2 - (5 * 50) // 2, HEIGHT // 2 - (5 * 50) // 2, 5, 5, 50, 50, win
    )
    maze._break_walls_r(0, 0)  # just to test the method to make paths

    # wait for the window to close
    win.wait_for_close()


if __name__ == "__main__":
    main()
