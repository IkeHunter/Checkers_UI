from checkers_functions import CheckersBridge as Bridge
import random


class RandomAgent:

    def __init__(self, player):
        self.env = Bridge()
        self.player = player

    def reset_board(self):
        self.env.reset()

    def random_turn(self):
        pieces = []

        if self.player == 1:
            pieces.append(1)
            pieces.append(3)
        else:
            pieces.append(2)
            pieces.append(4)

        # piece = random.choice(pieces)

        available_moves = self.env.available()

        if available_moves[pieces[1]]:
            piece = random.choice(pieces)
        else:
            piece = pieces[0]

        available_moves = available_moves[piece]

        move_index = random.randint(len(available_moves.keys))
        chosen_move = available_moves[move_index]

        self.env.step(chosen_move, piece)

    def loop(self):
        pass


