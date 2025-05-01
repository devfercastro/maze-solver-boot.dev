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

    # wait for the window to close
    win.wait_for_close()


if __name__ == "__main__":
    main()
