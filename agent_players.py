import random
import piece_player as player


class AgentPlayer:

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

    def _play_piece(self):
        piece_moves, king_moves = self.player.available_moves()
        available_moves = [piece_moves, king_moves]
        # print("\nAvailable Moves: {}\n".format(available_moves))
        print("\n")
        for i in range(len(available_moves)):
            if i == 0:
                print("({}) Pawns: {}".format(self.piece, available_moves[i]))
            if i == 1:
                print("({}) Kings: {}".format(self.piece, available_moves[i]))

        if available_moves[0] and available_moves[1]:
            play_piece = random.randint(0, 1)
        elif available_moves[0] and not available_moves[1]:
            play_piece = 0
        elif not available_moves[0] and available_moves[1]:
            play_piece = 1
        else:
            play_piece = None

        if play_piece is not None:
            available_moves = available_moves[play_piece]
        else:
            available_moves = None

        return available_moves

    def chose_random_turn(self, moves):
        if not moves:
            self.done = True
            chosen_move = None
        else:
            if len(moves.keys()) == 1:
                move_index = 0
            else:
                move_index = random.randint(0, len(moves.keys()) - 1)

            chosen_move = moves[move_index]

        return chosen_move


class RandomAgent(AgentPlayer):

    def __init__(self, piece, game, env):
        super().__init__(piece, game, env)

    def random_turn(self):
        """Handles moving the piece"""

        available_moves = self._play_piece()
        # print("available moves: " + str(available_moves))  # TODO: print

        chosen_move = self.chose_random_turn(available_moves)

        _, _, self.done, _ = self.env.step(chosen_move, self.piece)

        return self.done

    def random_move(self):
        """Returns random moves to be passed into env"""

        available_moves = self._play_piece()
        print("\navailable moves: {}\n".format(available_moves))  # TODO: print

        if available_moves:
            chosen_move = self.chose_random_turn(available_moves)
        else:
            chosen_move = None

        return chosen_move


class OffensiveAgent(AgentPlayer):

    def __init__(self, piece, game, env):
        super().__init__(piece, game, env)

    def offensive_turn(self):
        """Handles moving the piece"""

        available_moves = self._play_piece()

        offensive_moves = []

        for i in available_moves:
            if available_moves[i]['row_jumped']:
                offensive_moves.append(available_moves[i])

        if not offensive_moves:
            chosen_move = self.chose_random_turn(available_moves)
        else:
            if len(offensive_moves) == 1:
                move_index = 0
            else:
                move_index = random.randint(0, len(offensive_moves) - 1)

            chosen_move = offensive_moves[move_index]

        _, _, self.done, _ = self.env.step(chosen_move, self.piece)

        return self.done

    def offensive_move(self):
        """Returns random moves to be passed into env"""

        available_moves = self._play_piece()

        if available_moves:
            offensive_moves = []

            for i in available_moves:
                if available_moves[i]['row_jumped']:
                    offensive_moves.append(available_moves[i])

            if not offensive_moves:
                chosen_move = self.chose_random_turn(available_moves)
            else:
                if len(offensive_moves) == 1:
                    move_index = 0
                else:
                    move_index = random.randint(0, len(offensive_moves) - 1)

                chosen_move = offensive_moves[move_index]
        else:
            chosen_move = None

        return chosen_move

