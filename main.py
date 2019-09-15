import checkers_game as cg
import agent_random as ag
import checkers_environment as ce


def main():
    # checkers = cg.CheckerBoard()
    #
    # # checkers.move_piece(5, 2, 4, 3, 2, None)
    # # checkers.move_piece(2, 5, 3, 4, 1, None)
    # # jumped = {'row': 3, 'col': 4}
    # # checkers.move_piece(4, 3, 2, 5, 2, jumped)
    # # checkers.move_piece(0, 5, 3, 0, 1, None)
    # # checkers.move_piece(2, 5, 0, 5, 2, None)
    #
    # checkers.render_board()
    # checkers.game_logic.available_moves()

    board = cg.CheckerBoard()
    env = ce.CheckersBridge(board)

    random_agent_1 = ag.RandomAgent(1, board, env)
    random_agent_2 = ag.RandomAgent(2, board, env)

    win = board.check_win()

    while win == 0:
        board.render_board()
        random_agent_1.random_turn()
        random_agent_2.random_turn()
        win = board.check_win()


    print("{} wins!".format(str(win)))


if __name__ == '__main__':
    main()
