import checkers_gui as gui
import tkinter


def main():
    checkers = gui.CheckersLogic()

    main_window = tkinter.Tk()
    checkers.main_loop(main_window)

    checkers.move_piece(5, 0, 4, 1, 2)

    main_window.mainloop()


if __name__ == '__main__':
    main()
