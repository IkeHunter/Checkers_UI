class Player:
    def __init__(self, piece, game):
        self.game = game

        if piece is 1 or piece is 2:
            self.piece = piece
        else:
            raise Exception('Arg must be 1 or 2, not {} of type {}'.format(str(piece), type(piece)))

        self.available_pieces = []
        if self.piece == 1:
            self.available_pieces.append(1)
            self.available_pieces.append(3)
            self.king = 3
        else:
            self.available_pieces.append(2)
            self.available_pieces.append(4)
            self.king = 4

    def available_moves(self):
        piece_moves = self.game.get_moves(self.piece)
        king_moves = self.game.get_moves(self.king)
        return piece_moves, king_moves

    def get_pieces(self):
        return self.available_pieces
