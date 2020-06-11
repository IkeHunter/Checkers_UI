import json
import copy


class CheckersBridge:

    def __init__(self, game):
        self.game = game
        self.gui = game.game_gui
        self.game_moves = []

    @staticmethod
    def write_move_file(move_dict):

        def file_write():
            with open('moves', 'w') as move_file:
                json.dump(move_dict, move_file)

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

            if self.game_moves:
                self.game_moves.append(copy.deepcopy(self.game.current_board))
            else:
                self.game_moves = [copy.deepcopy(self.game.current_board)]

            print("\n")
            for key in self.game.current_board.keys():
                print(self.game.current_board[key])
            print("\n")

            self.write_move_file(self.game_moves)

            done = self.has_won()

        else:
            done = True

        self.sync_gui_stats()
        return obs, reward, done, info

    def has_won(self):
        status = self.game.check_win()
        # if status == 1:
        #     agent_status = True
        # else:
        #     agent_status = False

        if not status == 0:
            return True
        else:
            return False

        # return status, agent_status
