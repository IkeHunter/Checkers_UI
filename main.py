import checkers_gui as gui
import checkers_game as cg
import tkinter


def main():
    checkers_board = dict()

    checkers = gui.CheckersUI(checkers_board)
    main_window = tkinter.Tk()
    checkers.move_piece(5, 0, 4, 1, 2)
    # checkers.move_piece(5, 2, 4, 3, 2)
    # checkers.move_piece(5, 4, 4, 5, 2)
    # checkers.move_piece(5, 6, 4, 7, 2)
    checkers_board = checkers.main_loop(main_window)

    print("the board: " + str(checkers_board))

    main_window.mainloop()
    cg.CheckersLogic(checkers_board).available_moves()


if __name__ == '__main__':
    main()
