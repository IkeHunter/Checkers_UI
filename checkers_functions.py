import checkers_game as cg


class CheckersBridge:

    def __init__(self):
        self.game = cg.CheckerBoard()

    def reset(self):
        self.game.reset_board()

    def render(self):
        self.game.render_board()

    def step(self, move: dict, jumped):
        self.game.move_piece(move, jumped)

    def has_won(self):
        status = self.game.check_win()
        if status == 1:
            ai_status = True
        else:
            ai_status = False

        return status, ai_status
