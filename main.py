from window import Window


def main():
    # create a window
    win = Window(800, 600)
    # and wait for it to close
    win.wait_for_close()


if __name__ == "__main__":
    main()
