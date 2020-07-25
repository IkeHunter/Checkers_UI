class CheckersLogic:

    def __init__(self, board):
        self.board = board

    def iter_dict(self, target):
        for row in range(len(self.board.keys())):
            for col in range(len(self.board[row])):
                if self.board[row][col] == target:
                    return True
        return False

    def pieces_coord(self, piece):
        """creates a dict of coordinates of pieces"""
        if piece in range(1, 5):
            board_dict = self.board
            pieces = dict()
            for row in range(len(board_dict)):
                for col in range(len(board_dict[row])):
                    if self.board[row][col] == piece:
                        if not pieces:
                            num = 0
                        else:
                            num = len(pieces)
                        item = {num: {'row': row, 'col': col}}
                        pieces.update(item)
            return pieces
        else:
            raise Exception('While creating piece dict: The piece needs to be 1-4, got {} of type {}'
                            .format(str(piece), type(piece)))

    @staticmethod
    def num_iter(available_coords_dict):
        if not available_coords_dict:
            num_iter_var = 0
        else:
            num_iter_var = len(available_coords_dict)
        return num_iter_var

    def available_moves(self):
        board_pieces = []
        available_coords_all = {
            1: None,
            2: None,
            3: None,
            4: None
        }
        available_coords_one = dict()
        available_coords_two = dict()
        available_coords_three = dict()
        available_coords_four = dict()

        for i in range(1, 5):
            piece = self.iter_dict(i)
            if piece:
                board_pieces.append(i)

        if 1 in board_pieces:
            available_coords_one = self.available_one()
        if 2 in board_pieces:
            available_coords_two = self.available_two()
        if 3 in board_pieces:
            available_coords_three = self.available_king(3)
        if 4 in board_pieces:
            available_coords_four = self.available_king(4)

        available_coords_all[1] = available_coords_one
        available_coords_all[2] = available_coords_two
        available_coords_all[3] = available_coords_three
        available_coords_all[4] = available_coords_four

        return available_coords_all

    def available_one(self):
        pieces = self.pieces_coord(1)
        available_coords_one = dict()
        for i in range(len(pieces.keys())):
            row_coord = pieces[i]['row']
            col_coord = pieces[i]['col']

            try:
                row_coord_move = row_coord + 1
                row_coord_jump = row_coord + 2

                col_coord_move_one = col_coord - 1
                col_coord_move_two = col_coord + 1
                col_coord_jump_one = col_coord - 2
                col_coord_jump_two = col_coord + 2

                if row_coord_move >= 0 and col_coord_move_one >= 0:
                    if self.board[row_coord_move][col_coord_move_one] == 0:
                        num = self.num_iter(available_coords_one)
                        available_coords_one.update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                           'row_to': row_coord_move, 'col_to': col_coord_move_one,
                                                           'row_jumped': None, 'col_jumped': None,
                                                           'piece': 1}})
                    elif self.board[row_coord_move][col_coord_move_one] == 2 \
                            and self.board[row_coord_jump][col_coord_jump_one] == 0:
                        if row_coord_jump >= 0 and col_coord_jump_one >= 0:
                            num = self.num_iter(available_coords_one)
                            available_coords_one.update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                               'row_to': row_coord_jump, 'col_to': col_coord_jump_one,
                                                               'row_jumped': row_coord_move,
                                                               'col_jumped': col_coord_move_one,
                                                               'piece': 1}})
                if row_coord_move >= 0 and col_coord_move_two >= 0:
                    if self.board[row_coord_move][col_coord_move_two] == 0:
                        num = self.num_iter(available_coords_one)
                        available_coords_one.update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                           'row_to': row_coord_move, 'col_to': col_coord_move_two,
                                                           'row_jumped': None, 'col_jumped': None,
                                                           'piece': 1}})
                    elif self.board[row_coord_move][col_coord_move_one] == 2 \
                            and self.board[row_coord_jump][col_coord_jump_two] == 0:
                        if row_coord_jump >= 0 and col_coord_jump_two >= 0:
                            num = self.num_iter(available_coords_one)
                            available_coords_one.update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                               'row_to': row_coord_jump, 'col_to': col_coord_jump_two,
                                                               'row_jumped': row_coord_move,
                                                               'col_jumped': col_coord_move_two,
                                                               'piece': 1}})

            except IndexError:
                continue

            except KeyError:
                continue

        return available_coords_one

    def available_two(self):
        pieces = self.pieces_coord(2)
        available_coords_two = dict()
        for i in range(len(pieces.keys())):
            row_coord = pieces[i]['row']
            col_coord = pieces[i]['col']

            try:
                row_coord_move = row_coord - 1
                row_coord_jump = row_coord - 2

                col_coord_move_one = col_coord - 1
                col_coord_move_two = col_coord + 1
                col_coord_jump_one = col_coord - 2
                col_coord_jump_two = col_coord + 2

                if row_coord_move >= 0 and col_coord_move_one >= 0:

                    if self.board[row_coord_move][col_coord_move_one] == 0:
                        num = self.num_iter(available_coords_two)
                        available_coords_two.update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                           'row_to': row_coord_move, 'col_to': col_coord_move_one,
                                                           'row_jumped': None, 'col_jumped': None,
                                                           'piece': 2}})
                    elif self.board[row_coord_move][col_coord_move_one] == 1 \
                            and self.board[row_coord_jump][col_coord_jump_one] == 0:
                        if row_coord_jump >= 0 and col_coord_jump_one >= 0:
                            num = self.num_iter(available_coords_two)
                            available_coords_two.update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                               'row_to': row_coord_jump, 'col_to': col_coord_jump_one,
                                                               'row_jumped': row_coord_move,
                                                               'col_jumped': col_coord_move_one,
                                                               'piece': 2}})
                if row_coord_move >= 0 and col_coord_move_two >= 0:
                    if self.board[row_coord_move][col_coord_move_two] == 0:
                        num = self.num_iter(available_coords_two)
                        available_coords_two.update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                           'row_to': row_coord_move, 'col_to': col_coord_move_two,
                                                           'row_jumped': None, 'col_jumped': None,
                                                           'piece': 2}})
                    elif self.board[row_coord_move][col_coord_move_two] == 1 \
                            and self.board[row_coord_jump][col_coord_jump_two] == 0:
                        if row_coord_jump >= 0 and col_coord_jump_two >= 0:
                            num = self.num_iter(available_coords_two)
                            available_coords_two.update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                               'row_to': row_coord_jump, 'col_to': col_coord_jump_two,
                                                               'row_jumped': row_coord_move,
                                                               'col_jumped': col_coord_move_two,
                                                               'piece': 2}})

            except IndexError:
                continue

            except KeyError:
                continue

        return available_coords_two

    def available_king(self, number_piece):
        pieces = self.pieces_coord(number_piece)
        available_coords_king = dict()

        enemy_piece = []
        if number_piece == 3:
            enemy_piece.append(2)
            enemy_piece.append(4)
        elif number_piece == 4:
            enemy_piece.append(1)
            enemy_piece.append(3)

        for i in range(len(pieces.keys())):
            row_coord = pieces[i]['row']
            col_coord = pieces[i]['col']

            row_coord_move_one = row_coord - 1
            row_coord_move_two = row_coord + 1
            row_coord_jump_one = row_coord - 2
            row_coord_jump_two = row_coord + 2

            col_coord_move_one = col_coord - 1
            col_coord_move_two = col_coord + 1
            col_coord_jump_one = col_coord - 2
            col_coord_jump_two = col_coord + 2

            row_list = [row_coord_move_one, row_coord_move_two]
            col_list = [col_coord_move_one, col_coord_move_two]
            row_jump_list = [row_coord_jump_one, row_coord_jump_two]
            col_jump_list = [col_coord_jump_one, col_coord_jump_two]

            for j in range(2):
                for h in range(2):
                    try:
                        if self.board[row_list[j]][col_list[h]] == 0:
                            if (8 > row_list[j] > 0) and (8 > col_list[h] > 0):
                                num = self.num_iter(available_coords_king)

                                available_coords_king.update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                                    'row_to': row_list[j], 'col_to': col_list[h],
                                                                    'row_jumped': None, 'col_jumped': None,
                                                                    'piece': number_piece}})

                        elif self.board[row_list[j]][col_list[h]] in enemy_piece \
                                and self.board[row_jump_list[j]][col_jump_list[h]] == 0:
                            if (8 > row_jump_list[j] > 0) and (8 > col_jump_list[h] > 0):
                                num = self.num_iter(available_coords_king)

                                available_coords_king \
                                    .update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                   'row_to': row_jump_list[j], 'col_to': col_jump_list[h],
                                                   'row_jumped': row_list[j], 'col_jumped': col_list[h],
                                                   'piece': number_piece}})

                    except IndexError:
                        continue
                    except KeyError:
                        continue

        return available_coords_king
