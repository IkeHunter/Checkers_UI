import checkers_game as cg
import agent_random as ag
import checkers_environment as ce

import tkinter as tk


def main():
    main_window = tk.Tk()
    board = cg.CheckerBoard(main_window)
    env = ce.CheckersBridge(board)

    board.set_up_board()

    random_agent_1 = ag.RandomAgent(1, board, env)
    random_agent_2 = ag.RandomAgent(2, board, env)

    def game_loop_1():
        board.render_board()
        win = board.check_win()

        if not win > 0:
            random_agent_1.random_turn()
            main_window.after(500, game_loop_2)
        else:
            print("{} wins!")
            main_window.after(3000)

    def game_loop_2():
        board.render_board()
        win = board.check_win()

        if not win > 0:
            random_agent_2.random_turn()
            main_window.after(500, game_loop_1)
        else:
            print("{} wins!")

    main_window.after(1000, game_loop_1)
    main_window.mainloop()


if __name__ == '__main__':
    main()
