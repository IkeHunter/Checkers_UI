import tkinter


class CheckersGUI:

    def __init__(self):
        self.board = CheckerBoard()

    def config(self, main_window):
        board_obj = self.board.get_board()
        for board_row in range(len(board_obj.keys())):
            main_window.rowconfigure(board_row, weight=1)
            for board_col in range(len(board_obj[board_row])):
                main_window.columnconfigure(board_col, weight=1)

    def board_setup(self, main_window):
        self.board = self.board.start_board()
        board_grid = dict()

        def add_box(grid, box_var, i):
            grid[i] = [box_var]

            return grid

        for board_row in range(len(self.board.keys())):
            board_grid.update({board_row: 0})
            for board_col in range(len(self.board[board_row])):
                if self.board[board_row][board_col] == 5:
                    box = tkinter.Label(main_window, padx=12, pady=12, bg='black', text=" ")\
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)
                elif self.board[board_row][board_col] == 0:
                    box = tkinter.Label(main_window, padx=12, pady=12, bg='white', text=" ")\
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)
                elif self.board[board_row][board_col] == 1:
                    text_opts = ("Helvetica", 35, 'bold')
                    box = tkinter.Label(main_window, padx=0, pady=0, bg='white', text='O', font=text_opts, fg='blue')\
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)
                elif self.board[board_row][board_col] == 2:
                    text_opts = ("Helvetica", 35, 'bold')
                    box = tkinter.Label(main_window, padx=0, pady=0, bg='white', text='O', font=text_opts, fg='red')\
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)

    def main_loop(self, main_window):
        main_window.title("Checkers")
        main_window.geometry('900x900-80-100')
        self.config(main_window)
        self.board_setup(main_window)


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
        self.start_board()

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

    def print_board(self):
        for i in range(len(self.board_dict.keys())):
            print(self.board_dict[i])
