import checkers_game as cg
import numpy as np


class CheckersBridge:

    def __init__(self):
        self.game = cg.CheckerBoard()

    def reset(self):
        self.game.reset_board()

    def available(self):
        moves = self.game.game_logic.available_moves()

        return moves

    def render(self):
        self.game.render_board()

    def step(self, move: dict, jumped):
        obs = None
        reward = None
        info = None
        self.game.move_piece(move, jumped)

        _, done = self.has_won()

        return obs, reward, done, info

    def has_won(self):
        status = self.game.check_win()
        if status == 1:
            agent_status = True
        else:
            agent_status = False

        return status, agent_status


# board = CheckersBridge()
# board.available()