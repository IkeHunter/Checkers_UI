import random
import piece_player as player


class RandomAgent:

    """
    game -> random agent -> env -> board
                |
              player
    """

    def __init__(self, piece, game, env):
        self.piece = piece
        self.env = env
        self.player = player.Player(self.piece, game)
        self.done = False

    def random_turn(self):

        piece_moves, king_moves = self.player.available_moves()
        available_moves = [piece_moves, king_moves]

        if available_moves[1]:
            play_piece = random.randint(0, 2)
        else:
            play_piece = 0

        available_moves = available_moves[play_piece]
        # print(available_moves)
        # print(type(available_moves))
        # print(len(available_moves.keys()))

        # print(len(available_moves.keys()))
        print(available_moves)
        # print(len(available_moves.keys()))

        move_index = random.randint(0, len(available_moves.keys()) - 1)

        print("length: {} chosen: {}".format(len(available_moves.keys()), move_index))
        chosen_move = available_moves[move_index]

        _, _, self.done, _ = self.env.step(chosen_move, self.piece)



