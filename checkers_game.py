import checkers_gui as gui


class CheckerBoard:

    def __init__(self):

        self.board_dict = {  # 0 = can move to space, 5 = cannot move to space
            0: [5, 0, 5, 0, 5, 0, 5, 0],
            1: [0, 5, 0, 5, 0, 5, 0, 5],
            2: [5, 0, 5, 0, 5, 0, 5, 0],
            3: [0, 5, 0, 5, 0, 5, 0, 5],
            4: [5, 0, 5, 0, 5, 0, 5, 0],
            5: [0, 5, 0, 5, 0, 5, 0, 5],
            6: [5, 0, 5, 0, 5, 0, 5, 0],
            7: [0, 5, 0, 5, 0, 5, 0, 5]
        }
        self.current_board = self.board_dict
        self.check_board()
        self.jumped_pieces = {
            1: 0,
            2: 0
        }
        self.king_pieces = {
            1: 0,
            2: 0
        }
        self.game_logic = CheckersLogic(self.current_board)
        self.game_gui = gui.CheckersUI(self.current_board, self.jumped_pieces, self.king_pieces)

    def get_board(self):
        return self.current_board

    def start_board(self):
        for i in range(len(self.current_board.keys())):
            # if i <= 2 or i >= 5:
            if i <= 2:
                for j in range(len(self.current_board[i])):
                    if self.board_dict[i][j] == 0:
                        self.current_board[i][j] = 1
            elif i >= 5:
                for j in range(len(self.current_board[i])):
                    if self.current_board[i][j] == 0:
                        self.current_board[i][j] = 2

    def check_board(self):
        if self.current_board == self.board_dict:
            self.start_board()

    def move_piece(self, y_from, x_from, y_to, x_to, piece, jumped):  # TODO: move piece raises exceptions
        # jumped is a dict
        if piece in range(1, 5):
            if y_from in range(0, 8) and x_from in range(0, 8):
                self.current_board[y_from][x_from] = 0
            else:
                raise Exception('X or Y from values do not match dict, X: {}, Y: {}'.format(str(x_from), str(y_from)))
            if y_to in range(0, 8) and x_to in range(0, 8):
                self.current_board[y_to][x_to] = piece
                if jumped:
                    self.piece_jumped(jumped)
                # board[4][3] = 4
                # board[3][4] = 3

                self.piece_king_status()
                return self.current_board
            else:
                raise Exception('X or Y to values do not match dict, x: {}, y: {}'.format(str(x_to), str(y_to)))
        else:
            raise Exception('Piece should be int 0 < x < 5, instead got {} of type {}'.format(str(piece), type(piece)))

    def piece_jumped(self, piece):
        row = piece['row']
        col = piece['col']
        piece_val = self.current_board[row][col]
        if piece_val == 3:
            piece_val = 1
        elif piece_val == 4:
            piece_val = 2

        self.current_board[row][col] = 0

        self.jumped_pieces[piece_val] += 1

    def print_board(self):
        for i in range(len(self.board_dict.keys())):
            print(self.board_dict[i])

    def check_status(self, board):
        state_list = []
        if board is None:
            return False
        else:
            for i in range(len(self.board_dict.keys())):
                for j in range(len(self.board_dict[i])):
                    if board[i][j] not in state_list:
                        state_list.append(board[i][j])
            if len(state_list) <= 2:
                return False
            else:
                return True

    def piece_king_status(self):
        row_zero = self.current_board[0]
        row_seven = self.current_board[7]
        for col in range(len(row_seven)):
            if row_seven[col] == 1:  # if piece 1 in col and row 7, to king
                self.current_board[7][col] = 3
                self.king_pieces[1] += 1
        for col in range(len(row_zero)):
            if row_zero[col] == 2:  # if piece 2 in col and row 0, to king
                self.current_board[0][col] = 4
                self.king_pieces[2] += 1

    def board_iter(self):
        board_pieces = []
        for i in range(1, 5):
            piece = self.game_logic.iter_dict(i)
            if piece:
                board_pieces.append(i)
        return board_pieces

    def check_win(self):
        board_pieces = self.board_iter()
        if 1 not in board_pieces and 3 not in board_pieces:
            return 2
        elif 2 not in board_pieces and 4 not in board_pieces:
            return 1
        else:
            return 0


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
        available_coords_one = dict()
        available_coords_two = dict()
        available_coords_three = dict()
        available_coords_four = dict()
        kings_list = [available_coords_three, available_coords_four]

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

        if available_coords_one:
            print("available coords for one: " + str(available_coords_one))
        else:
            print("No moves for one")

        if available_coords_two:
            print("available coords for two: " + str(available_coords_two))
        else:
            print("No moves for two")

        if available_coords_three:
            print("available coords for three: " + str(available_coords_three))
        else:
            print("No moves for three")

        if available_coords_four:
            print("available coords for four: " + str(available_coords_four))
        else:
            print("No moves for four")

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
                                                           'row_jumped': None, 'col_jumped': None}})
                    elif self.board[row_coord_move][col_coord_move_one] == 2 \
                            and self.board[row_coord_jump][col_coord_jump_one] == 0:
                        if row_coord_jump >= 0 and col_coord_jump_one >= 0:
                            num = self.num_iter(available_coords_one)
                            available_coords_one.update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                               'row_to': row_coord_jump, 'col_to': col_coord_jump_one,
                                                               'row_jumped': row_coord_move,
                                                               'col_jumped': col_coord_move_one}})
                if row_coord_move >= 0 and col_coord_move_two >= 0:
                    if self.board[row_coord_move][col_coord_move_two] == 0:
                        num = self.num_iter(available_coords_one)
                        available_coords_one.update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                           'row_to': row_coord_move, 'col_to': col_coord_move_two,
                                                           'row_jumped': None, 'col_jumped': None}})
                    elif self.board[row_coord_move][col_coord_move_one] == 2 \
                            and self.board[row_coord_jump][col_coord_jump_two] == 0:
                        if row_coord_jump >= 0 and col_coord_jump_two >= 0:
                            num = self.num_iter(available_coords_one)
                            available_coords_one.update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                               'row_to': row_coord_jump, 'col_to': col_coord_jump_two,
                                                               'row_jumped': row_coord_move,
                                                               'col_jumped': col_coord_move_two}})


            except IndexError:
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
                                                           'row_jumped': None, 'col_jumped': None}})
                    elif self.board[row_coord_move][col_coord_move_one] == 1 \
                            and self.board[row_coord_jump][col_coord_jump_one] == 0:
                        if row_coord_jump >= 0 and col_coord_jump_one >= 0:
                            num = self.num_iter(available_coords_two)
                            available_coords_two.update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                               'row_to': row_coord_jump, 'col_to': col_coord_jump_one,
                                                               'row_jumped': row_coord_move,
                                                               'col_jumped': col_coord_move_one}})
                if row_coord_move >= 0 and col_coord_move_two >= 0:
                    if self.board[row_coord_move][col_coord_move_two] == 0:
                        num = self.num_iter(available_coords_two)
                        available_coords_two.update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                           'row_to': row_coord_move, 'col_to': col_coord_move_two,
                                                           'row_jumped': None, 'col_jumped': None}})
                    elif self.board[row_coord_move][col_coord_move_two] == 1 \
                            and self.board[row_coord_jump][col_coord_jump_two] == 0:
                        if row_coord_jump >= 0 and col_coord_jump_two >= 0:
                            num = self.num_iter(available_coords_two)
                            available_coords_two.update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                               'row_to': row_coord_jump, 'col_to': col_coord_jump_two,
                                                               'row_jumped': row_coord_move,
                                                               'col_jumped': col_coord_move_two}})

            except IndexError:
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

            if row_coord_move_one >= 0 and row_coord_move_two >= 0 and row_coord_jump_one >= 0 and row_coord_move_two >= 0 and col_coord_move_one >= 0 and col_coord_move_two >= 0 \
                    and col_coord_jump_one >= 0 and col_coord_jump_two >= 0:
                for j in range(2):
                    for h in range(2):
                        try:
                            if self.board[row_list[j]][col_list[h]] == 0:
                                num = self.num_iter(available_coords_king)

                                available_coords_king.update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                                    'row_to': row_list[j], 'col_to': col_list[h]}})

                            elif self.board[row_list[j]][col_list[h]] in enemy_piece \
                                    and self.board[row_jump_list[j]][col_jump_list[h]] == 0:
                                num = self.num_iter(available_coords_king)

                                available_coords_king \
                                    .update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                   'row_to': row_jump_list[j], 'col_to': col_jump_list[h]}})

                        except IndexError:
                            continue

        return available_coords_king