import numpy as np
import pickle


class CheckersBridge:

    def __init__(self, game):
        self.game = game
        self.gui = game.game_gui

    @staticmethod
    def write_move_file(move_dict):

        def file_write():
            with open('moves.pkl', 'wb') as move_file:
                pickle.dump(move_dict, move_file)

        file_write()


    def sync_gui_stats(self):
        self.gui.move_count = self.game.move_count
        self.gui.kings = self.game.king_pieces
        self.gui.jumps = self.game.jumped_pieces

    def reset(self):
        self.game.reset_board()
        self.game.set_up_board()
        # self.game.print_board()

    # def available(self):
    #     moves = self.game.game_logic.available_moves()
    #
    #     return moves

    def render(self):
        self.game.render_board()

    def step(self, move, piece):
        obs = None
        reward = None
        info = None
        if move:
            self.game.move_piece(move)
            self.write_move_file(move)

        _, done = self.has_won()

        self.sync_gui_stats()
        return obs, reward, done, info

    def has_won(self):
        status = self.game.check_win()
        if status == 1:
            agent_status = True
        else:
            agent_status = False

        return status, agent_status


# board = CheckersBridge()
# print(board.available())