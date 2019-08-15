import checkers_gui as gui
import checkers_game as cg
import tkinter


def main():
    checkers = cg.CheckerBoard()
    checkers_board = checkers.get_board()

    checkers_gui = checkers.game_gui
    main_window = tkinter.Tk()

    # checkers.move_piece(5, 2, 4, 3, 2, None)
    # checkers.move_piece(2, 5, 3, 4, 1, None)
    # jumped = {'row': 3, 'col': 4}
    # checkers.move_piece(4, 3, 2, 5, 2, jumped)
    # checkers.move_piece(0, 5, 3, 0, 1, None)
    # checkers.move_piece(2, 5, 0, 5, 2, None)

    checkers_gui.main_loop(main_window)

    print("the board: " + str(checkers_board))

    main_window.mainloop()
    checkers.game_logic.available_moves()


if __name__ == '__main__':
    main()
