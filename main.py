import checkers_game as cg
import agent_players as ag
import checkers_environment as ce

import tkinter as tk


def main():
    main_window = tk.Tk()
    board = cg.CheckerBoard(main_window)
    env = ce.CheckersBridge(board)

    board.set_up_board()

    random_agent_1 = ag.OffensiveAgent(1, board, env)
    random_agent_2 = ag.OffensiveAgent(2, board, env)

    def game_loop_1():
        frame = tk.Frame(main_window, bg='systemTransparent')
        frame.grid(row=0, column=0, sticky='nsew', columnspan=8, rowspan=8)
        frame = board.game_gui.config(board.current_board, frame, False)

        board.render_board(frame)
        win = board.check_win()

        if not win > 0:
            random_agent_1.offensive_turn()
            main_window.after(250, game_loop_2)
        else:
            if win == 1 or win == 2:
                print("{} wins!".format(str(win)))
            elif win == 5:
                print("No more moves!")
            main_window.after(3000)

    def game_loop_2():
        frame = tk.Frame(main_window, bg='systemTransparent')
        frame.grid(row=0, column=0, sticky='nsew', columnspan=8, rowspan=8)
        frame = board.game_gui.config(board.current_board, frame, False)

        board.render_board(frame)
        win = board.check_win()

        if not win > 0:
            random_agent_2.offensive_turn()
            main_window.after(250, game_loop_1)
        else:
            if win == 1 or win == 2:
                print("{} wins!".format(str(win)))
            elif win == 5:
                print("No more moves!")
            main_window.after(3000)

    main_window.after(1000, game_loop_1)
    main_window.mainloop()


if __name__ == '__main__':
    main()
