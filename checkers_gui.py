import tkinter

import checkers_game as cg


class CheckersUI:

    def __init__(self, board, jumped, kings, main_window):
        self.board_game = board
        self.jumped = jumped
        self.kings = kings
        self.main_window = main_window

    def set_up(self):
        self.main_window.title("Checkers")
        self.main_window.geometry('1100x1100-80-100')
        self.config()

    # def main_loop(self):
    #     self.main_window.after(2000, self.board_render)

    def config(self):
        board_obj = self.board_game
        for board_row in range(len(board_obj.keys())):
            self.main_window.rowconfigure(board_row, weight=1)
            for board_col in range(len(board_obj[board_row])):
                self.main_window.columnconfigure(board_col, weight=1)
        self.main_window.columnconfigure(8, weight=1)

    def board_render(self):
        board_ui = self.board_game
        board_grid = dict()

        def add_box(grid, box_var, i):
            grid[i] = [box_var]

            return grid

        for board_row in range(len(board_ui.keys())):
            board_grid.update({board_row: 0})
            for board_col in range(len(board_ui[board_row])):
                if board_ui[board_row][board_col] == 5:
                    box = tkinter.Label(self.main_window, padx=12, pady=12, bg='black', text=" ")\
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)
                elif board_ui[board_row][board_col] == 0:
                    box = tkinter.Label(self.main_window, padx=12, pady=12, bg='white', text=" ")\
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)
                elif board_ui[board_row][board_col] == 1:
                    text_opts = ("Helvetica", 35, 'bold')
                    box = tkinter.Label(self.main_window, padx=0, pady=0, bg='white', text='O', font=text_opts, fg='blue')\
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)
                elif board_ui[board_row][board_col] == 2:
                    text_opts = ("Helvetica", 35, 'bold')
                    box = tkinter.Label(self.main_window, padx=0, pady=0, bg='white', text='O', font=text_opts, fg='red')\
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)
                elif board_ui[board_row][board_col] == 3:
                    text_opts = ("Helvetica", 35, 'bold')
                    box = tkinter.Label(self.main_window, padx=0, pady=0, bg='white', text='X', font=text_opts, fg='blue')\
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)
                elif board_ui[board_row][board_col] == 4:
                    text_opts = ("Helvetica", 35, 'bold')
                    box = tkinter.Label(self.main_window, padx=0, pady=0, bg='white', text='X', font=text_opts, fg='red')\
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)

        text_opts = ("Helvetica", 23)

        text_jumped_one = "Jumped: {}".format(str(self.jumped[2]))
        text_jumped_two = "Jumped: {}".format(str(self.jumped[1]))
        text_kings_one = "Kings: {}".format(str(self.kings[1]))
        text_kings_two = "Kings: {}".format(str(self.kings[2]))

        label_frame = tkinter.LabelFrame(self.main_window, borderwidth=2, relief='solid')\
            .grid(row=0, column=8, rowspan=8, sticky='nsew')
        one_label = tkinter.Label(label_frame, bg='white', text=text_jumped_one, font=text_opts)\
            .grid(row=1, column=8, sticky='nsew', padx=2, pady=1)
        two_label = tkinter.Label(label_frame, bg='white', text=text_jumped_two, font=text_opts)\
            .grid(row=5, column=8, sticky='nsew', padx=2, pady=1)
        one_king = tkinter.Label(label_frame, bg='white', text=text_kings_one, font=text_opts)\
            .grid(row=2, column=8, sticky='nsew', padx=2, pady=1)
        two_king = tkinter.Label(label_frame, bg='white', text=text_kings_two, font=text_opts) \
            .grid(row=6, column=8, sticky='nsew', padx=2, pady=1)

        board_grid.update({8: [one_label], 9: [two_label]})


