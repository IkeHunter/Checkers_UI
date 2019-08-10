import tkinter

import checkers_game as cg


class CheckersUI:

    def __init__(self, board):
        self.board_class = cg.CheckerBoard()
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
                elif board_ui[board_row][board_col] == 3:
                    text_opts = ("Helvetica", 35, 'bold')
                    box = tkinter.Label(main_window, padx=0, pady=0, bg='white', text='X', font=text_opts, fg='blue')\
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)
                elif board_ui[board_row][board_col] == 4:
                    text_opts = ("Helvetica", 35, 'bold')
                    box = tkinter.Label(main_window, padx=0, pady=0, bg='white', text='X', font=text_opts, fg='red')\
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)

    def move_piece(self, y_from, x_from, y_to, x_to, piece):
        self.board_game = self.board_class.move_piece(y_from, x_from, y_to, x_to, piece, self.board_game)

