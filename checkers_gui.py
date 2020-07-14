import tkinter

import checkers_game as cg


class CheckersUI:

    def __init__(self, root_window):
        # self.board_game = board
        # self.jumped = jumped
        # self.kings = kings
        # self.move_count = move_count
        # self.main_window = main_frame
        self.main_window = root_window

    def set_up(self, board_game, root):
        root.title("Checkers")
        root.geometry('1100x1100-80-100')
        # frame.grid(sticky='nsew')
        self.config(board_game, root)

    # def main_loop(self):
    #     self.main_window.after(2000, self.board_render)

    def config(self, board_game, root):

        try:
            board_obj = board_game
            for board_row in range(len(board_obj.keys())):
                root.rowconfigure(board_row, weight=1)
                # frame.rowconfigure(board_row, weight=1)

                # print("range(len(board_obj[board_row] :: {} \nboard_row :: {} \nboard_obj[board_row] :: {}"
                #       .format(len(board_obj[board_row]), board_row, board_obj[board_row]))

                # print("range(len(board_obj[board_row] :: {} \nboard_row :: {} \nboard_obj[board_row] :: {}"
                #       .format(404, board_row, board_obj[str(board_row)]))

                for board_col in range(len(board_obj[board_row])):
                    root.columnconfigure(board_col, weight=1)
                    # frame.columnconfigure(board_col, weight=1)

            root.columnconfigure(8, weight=1)
            # frame.columnconfigure(8, weight=1)  # TODO: change col config to 7 for board_render() only

        except KeyError:
            board_obj = board_game
            for board_row in range(len(board_obj.keys())):
                root.rowconfigure(int(board_row), weight=1)
                # frame.rowconfigure(int(board_row), weight=1)

                for board_col in range(len(board_obj[str(board_row)])):
                    root.columnconfigure(board_col, weight=1)
                    # frame.columnconfigure(board_col, weight=1)
            root.columnconfigure(8, weight=1)
            # frame.columnconfigure(8, weight=1)  # TODO: change col config to 7 for board_render() only

        return root

    def board_render(self, board_ui, frame):
        # board_ui = self.board_game
        board_grid = dict()

        def add_box(grid, box_var, i):
            grid[i] = [box_var]

            return grid


        for board_row in board_ui.keys():
            board_grid.update({board_row: 0})
            for board_col in range(len(board_ui[board_row])):
                if board_ui[board_row][board_col] == 5:
                    box = tkinter.Label(frame, padx=12, pady=12, bg='black', text=" ") \
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)
                elif board_ui[board_row][board_col] == 0:
                    box = tkinter.Label(frame, padx=12, pady=12, bg='white', text=" ") \
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)
                elif board_ui[board_row][board_col] == 1:
                    text_opts = ("Helvetica", 35, 'bold')
                    box = tkinter.Label(frame, padx=0, pady=0, bg='white', text='O', font=text_opts,
                                        fg='blue') \
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)
                elif board_ui[board_row][board_col] == 2:
                    text_opts = ("Helvetica", 35, 'bold')
                    box = tkinter.Label(frame, padx=0, pady=0, bg='white', text='O', font=text_opts,
                                        fg='red') \
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)
                elif board_ui[board_row][board_col] == 3:
                    text_opts = ("Helvetica", 35, 'bold')
                    box = tkinter.Label(frame, padx=0, pady=0, bg='white', text='X', font=text_opts,
                                        fg='blue') \
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)
                elif board_ui[board_row][board_col] == 4:
                    text_opts = ("Helvetica", 35, 'bold')
                    box = tkinter.Label(frame, padx=0, pady=0, bg='white', text='X', font=text_opts,
                                        fg='red') \
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)

    def board_render_verbose(self, board_ui, jumped, kings, move_count):
        # board_ui = self.board_game
        board_grid = dict()

        def add_box(grid, box_var, i):
            grid[i] = [box_var]

            return grid

        for board_row in range(len(board_ui.keys())):
            board_grid.update({board_row: 0})
            for board_col in range(len(board_ui[board_row])):
                if board_ui[board_row][board_col] == 5:
                    box = tkinter.Label(self.main_window, padx=12, pady=12, bg='black', text=" ") \
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)
                elif board_ui[board_row][board_col] == 0:
                    box = tkinter.Label(self.main_window, padx=12, pady=12, bg='white', text=" ") \
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)
                elif board_ui[board_row][board_col] == 1:
                    text_opts = ("Helvetica", 35, 'bold')
                    box = tkinter.Label(self.main_window, padx=0, pady=0, bg='white', text='O', font=text_opts,
                                        fg='blue') \
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)
                elif board_ui[board_row][board_col] == 2:
                    text_opts = ("Helvetica", 35, 'bold')
                    box = tkinter.Label(self.main_window, padx=0, pady=0, bg='white', text='O', font=text_opts,
                                        fg='red') \
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)
                elif board_ui[board_row][board_col] == 3:
                    text_opts = ("Helvetica", 35, 'bold')
                    box = tkinter.Label(self.main_window, padx=0, pady=0, bg='white', text='X', font=text_opts,
                                        fg='blue') \
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)
                elif board_ui[board_row][board_col] == 4:
                    text_opts = ("Helvetica", 35, 'bold')
                    box = tkinter.Label(self.main_window, padx=0, pady=0, bg='white', text='X', font=text_opts,
                                        fg='red') \
                        .grid(row=board_row, column=board_col, sticky='nsew')
                    board_grid = add_box(board_grid, box, board_row)

        text_opts = ("Helvetica", 23)

        text_jumped_one = "Jumped: {}".format(str(jumped[2]))
        text_jumped_two = "Jumped: {}".format(str(jumped[1]))
        text_kings_one = "Kings: {}".format(str(kings[1]))
        text_kings_two = "Kings: {}".format(str(kings[2]))
        move_count = "Moves: {}".format(str(move_count))

        label_frame = tkinter.LabelFrame(self.main_window, borderwidth=2, relief='solid') \
            .grid(row=0, column=8, rowspan=8, sticky='nsew')
        one_label = tkinter.Label(label_frame, bg='white', text=text_jumped_one, font=text_opts) \
            .grid(row=1, column=8, sticky='nsew', padx=2, pady=1)
        two_label = tkinter.Label(label_frame, bg='white', text=text_jumped_two, font=text_opts) \
            .grid(row=5, column=8, sticky='nsew', padx=2, pady=1)
        one_king = tkinter.Label(label_frame, bg='white', text=text_kings_one, font=text_opts) \
            .grid(row=2, column=8, sticky='nsew', padx=2, pady=1)
        two_king = tkinter.Label(label_frame, bg='white', text=text_kings_two, font=text_opts) \
            .grid(row=6, column=8, sticky='nsew', padx=2, pady=1)
        move_label = tkinter.Label(label_frame, bg='white', text=move_count, font=text_opts) \
            .grid(row=3, column=8, sticky='nsew', padx=2, pady=1)

        board_grid.update({8: [one_label], 9: [two_label]})
