import json
import copy
import os


class CheckersBridge:

    def __init__(self, game):
        self.game = game
        self.gui = game.game_gui
        self.game_moves = []
        self.game_dict = {}

    @staticmethod
    def write_move_file(move_dict, game_index):
        with open('moves.json', 'r') as move_file:
            game_dict = json.load(move_file)

        with open('moves.json', 'w') as move_file:
            game_dict[game_index] = move_dict
            json.dump(game_dict, move_file)

    def sync_gui_stats(self):
        self.gui.move_count = self.game.move_count
        self.gui.kings = self.game.king_pieces
        self.gui.jumps = self.game.jumped_pieces

    def reset(self):
        self.game.reset_board()
        self.game.set_up_board()

    def render(self):
        self.game.render_board()

    def step(self, move, game_index=0):
        obs = None
        reward = None
        info = None

        if move:

            self.game.move_piece(move)

            if self.game_moves:
                self.game_moves.append(copy.deepcopy(self.game.current_board))
            else:
                self.game_moves = [copy.deepcopy(self.game.current_board)]

            self.write_move_file(self.game_moves, game_index)

            done = self.has_won()

        else:
            done = True

        self.sync_gui_stats()
        return obs, reward, done, info

    def has_won(self):
        status = self.game.check_win()

        if not status == 0:
            return True
        else:
            return False

