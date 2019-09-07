import random
import piece_player as player


class RandomAgent:

    def __init__(self, piece, game, env):
        # self.env = Bridge()
        self.env = env
        self.player = player.Player(piece, game)
        self.done = False

    # def reset_board(self):
    #     self.env.reset()

    def random_turn(self):
        # pieces = self.player.available_pieces

        # if self.player == 1:
        #     pieces.append(1)
        #     pieces.append(3)
        # else:
        #     pieces.append(2)
        #     pieces.append(4)

        # available_moves = self.env.available()

        piece_moves, king_moves = self.player.available_moves()
        available_moves = [piece_moves, king_moves]

        if available_moves[1]:
            # piece = random.choice(pieces)
            piece = random.randint(0, 2)
        else:
            # piece = pieces[0]
            piece = 0

        available_moves = available_moves[piece]

        move_index = random.randint(len(available_moves.keys))
        chosen_move = available_moves[move_index]

        _, _, self.done, _ = self.env.step(chosen_move, piece)



