import tkinter


class CheckersUI:

    def __init__(self, board):
        self.board_class = CheckerBoard()
        self.board_game = board
        self.check_board_status()

    def main_loop(self, main_window):
        main_window.title("Checkers")
        main_window.geometry('900x900-80-100')
        self.config(main_window)
        self.board_render(main_window)
        return self.board_game

    def check_board_status(self):
        if not self.board_game:
            self.board_game = self.board_class.start_board()

    def config(self, main_window):
        board_obj = self.board_class.get_board()
        for board_row in range(len(board_obj.keys())):
            main_window.rowconfigure(board_row, weight=1)
            for board_col in range(len(board_obj[board_row])):
                main_window.columnconfigure(board_col, weight=1)

    def board_render(self, main_window):
        board_ui = self.board_game
        board_grid = dict()

        def add_box(grid, box_var, i):
            grid[i] = [box_var]

            return grid

        for board_row in range(len(board_ui.keys())):
            board_grid.update({board_row: 0})
            for board_col in range(len(board_ui[board_row])):
                if board_ui[board_row][board_col] == 5:
                    box = tkinter.Label(main_window, padx=12, pady=12, bg='black', text=" ")\
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)
                elif board_ui[board_row][board_col] == 0:
                    box = tkinter.Label(main_window, padx=12, pady=12, bg='white', text=" ")\
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)
                elif board_ui[board_row][board_col] == 1:
                    text_opts = ("Helvetica", 35, 'bold')
                    box = tkinter.Label(main_window, padx=0, pady=0, bg='white', text='O', font=text_opts, fg='blue')\
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)
                elif board_ui[board_row][board_col] == 2:
                    text_opts = ("Helvetica", 35, 'bold')
                    box = tkinter.Label(main_window, padx=0, pady=0, bg='white', text='O', font=text_opts, fg='red')\
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)

    def move_piece(self, y_from, x_from, y_to, x_to, piece):
        self.board_game = self.board_class.move_piece(y_from, x_from, y_to, x_to, piece, self.board_game)


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
    def move_piece(y_from, x_from, y_to, x_to, piece, board):  # TODO: raises exceptions
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


