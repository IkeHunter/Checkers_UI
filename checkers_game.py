
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

    def get_board(self):
        return self.board_dict

    def start_board(self):
        for i in range(len(self.board_dict.keys())):
            # if i <= 2 or i >= 5:
            if i <= 2:
                for j in range(len(self.board_dict[i])):
                    if self.board_dict[i][j] == 0:
                        self.board_dict[i][j] = 1
            elif i >= 5:
                for j in range(len(self.board_dict[i])):
                    if self.board_dict[i][j] == 0:
                        self.board_dict[i][j] = 2

        return self.board_dict

    @staticmethod
    def move_piece(y_from, x_from, y_to, x_to, piece, board):  # TODO: move piece raises exceptions
        if piece in range(1, 5):
            if y_from in range(0, 8) and x_from in range(0, 8):
                board[y_from][x_from] = 0
            else:
                raise Exception('X or Y from values do not match dict, X: {}, Y: {}'.format(str(x_from), str(y_from)))
            if y_to in range(0, 8) and x_to in range(0, 8):
                board[y_to][x_to] = piece
                return board
            else:
                raise Exception('X or Y to values do not match dict, x: {}, y: {}'.format(str(x_to), str(y_to)))
        else:
            raise Exception('Piece should be int 0 < x < 5, instead got {} of type {}'.format(str(piece), type(piece)))



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


class CheckersLogic:

    def __init__(self, board):
        self.board = board
        self.board_dict = CheckerBoard().get_board()

    def iter_dict(self, target):
        for row in range(len(self.board.keys())):
            for col in range(len(self.board[row])):
                if self.board[row][col] == target:
                    return True
        return False

    def pieces_coord(self, piece):
        """creates a dict of coordinates of pieces"""
        if piece in range(1, 5):
            board_dict = self.board_dict
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
                col_coord_move_one = col_coord - 1
                col_coord_move_two = col_coord + 1

                num = self.num_iter(available_coords_one)

                if self.board[row_coord_move][col_coord_move_one] == 0:
                    available_coords_one.update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                       'row_to': row_coord_move, 'col_to': col_coord_move_one}})
                num = self.num_iter(available_coords_one)

                if self.board[row_coord_move][col_coord_move_two] == 0:
                    available_coords_one.update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                       'row': row_coord_move, 'col': col_coord_move_two}})
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
                col_coord_move_one = col_coord - 1
                col_coord_move_two = col_coord + 1

                num = self.num_iter(available_coords_two)

                if self.board[row_coord_move][col_coord_move_one] == 0:
                    available_coords_two.update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                       'row_to': row_coord_move, 'col_to': col_coord_move_one}})
                num = self.num_iter(available_coords_two)

                if self.board[row_coord_move][col_coord_move_two] == 0:
                    available_coords_two.update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                       'row': row_coord_move, 'col': col_coord_move_two}})
            except IndexError:
                continue

        return available_coords_two

    def available_king(self, number_piece):
        pieces = self.pieces_coord(number_piece)
        available_coords_king = dict()
        for i in range(len(pieces.keys())):
            row_coord = pieces[i]['row']
            col_coord = pieces[i]['col']

            row_coord_move_one = row_coord - 1
            row_coord_move_two = row_coord + 1
            col_coord_move_one = col_coord - 1
            col_coord_move_two = col_coord + 1

            row_list = [row_coord_move_one, row_coord_move_two]
            col_list = [col_coord_move_one, col_coord_move_two]

            for j in range(2):
                for h in range(2):
                    try:
                        if self.board[row_list[j]][col_list[h]] == 0:
                            num = self.num_iter(available_coords_king)

                            available_coords_king.update({num: {'row_from': row_coord, 'col_from': col_coord,
                                                                'row_to': row_list[j], 'col_to': col_list[h]}})
                    except IndexError:
                        continue

        return available_coords_king


