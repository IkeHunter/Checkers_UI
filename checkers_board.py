from checkers_ui import CheckersUI
from checkers_logic import CheckersLogic


class CheckersBoard:

    def __init__(self, main_window):

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
        self.move_count = 0
        self.max_moves = 750
        self.main_window = main_window
        self.game_logic = CheckersLogic(self.current_board)
        self.game_gui = CheckersUI()

    def get_board(self):
        return self.current_board

    def reset_board(self):
        self.current_board = self.board_dict
        self.start_board()

        self.jumped_pieces = {
            1: 0,
            2: 0
        }
        self.king_pieces = {
            1: 0,
            2: 0
        }
        self.move_count = 0

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

    def move_piece(self, move: dict):

        row_from = move['row_from']
        col_from = move['col_from']
        row_to = move['row_to']
        col_to = move['col_to']
        row_jumped = move['row_jumped']
        col_jumped = move['col_jumped']
        piece = move['piece']

        if piece in range(1, 5):
            if row_from in range(0, 8) and col_from in range(0, 8):
                self.current_board[row_from][col_from] = 0
            else:
                raise Exception('X or Y from values do not match dict, X: {}, Y: {}'
                                .format(str(col_from), str(row_from)))
            if row_to in range(0, 8) and col_to in range(0, 8):
                self.current_board[row_to][col_to] = piece
                if col_jumped and row_jumped:
                    self.piece_jumped(col_jumped, row_jumped)

                self.piece_king_status()
                self.move_count += 1
            else:
                raise Exception('X or Y to values do not match dict, x: {}, y: {}'.format(str(col_to), str(row_to)))

        else:
            raise Exception('Piece should be int 0 < x < 5, instead got {} of type {}'.format(str(piece), type(piece)))

    def piece_jumped(self, col, row):
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
        elif self.move_count > self.max_moves:
            return 5
        else:
            return 0

    def set_up_board(self):
        self.game_gui.set_up(self.current_board, self.main_window)

    def render_board(self, frame, main_window):
        self.game_gui.board_main_render(frame, main_window, self.current_board,
                                        self.jumped_pieces, self.king_pieces, self.move_count)

    def get_moves(self, piece):
        if piece not in range(1, 5):
            raise Exception('Get moves failed, piece {} not in range!'.format(piece))
        else:
            available_moves = self.game_logic.available_moves()

            if piece == 1:
                available_moves = available_moves[1]
            elif piece == 2:
                available_moves = available_moves[2]
            elif piece == 3:
                available_moves = available_moves[3]
            elif piece == 4:
                available_moves = available_moves[4]

            for i in available_moves:
                if (8 > available_moves[i]['row_from'] < 0) or (8 > available_moves[i]['row_to'] < 0) \
                        or (8 > available_moves[i]['col_from'] < 0) or (8 > available_moves[i]['col_to'] < 0):
                    raise Exception("Move Error: {}".format(available_moves[i]))

            return available_moves
