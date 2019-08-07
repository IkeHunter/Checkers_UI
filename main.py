import checkers_game as gui
import tkinter


def main():
    checkers_board = dict()

    checkers = gui.CheckersUI(checkers_board)
    main_window = tkinter.Tk()
    checkers.move_piece(5, 0, 4, 1, 2)
    checkers_board = checkers.main_loop(main_window)

    main_window.mainloop()


if __name__ == '__main__':
    main()
