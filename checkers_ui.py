import tkinter


class CheckersUI:

    @staticmethod
    def config(board_game, root, full):

        if full:
            config_int = 8
        else:
            config_int = 7

        try:
            board_obj = board_game
            for board_row in range(len(board_obj.keys())):
                root.rowconfigure(board_row, weight=1)

                for board_col in range(len(board_obj[board_row])):
                    root.columnconfigure(board_col, weight=1)

            root.columnconfigure(config_int, weight=1)

        except KeyError:
            board_obj = board_game
            for board_row in range(len(board_obj.keys())):
                root.rowconfigure(int(board_row), weight=1)

                for board_col in range(len(board_obj[str(board_row)])):
                    root.columnconfigure(board_col, weight=1)

            root.columnconfigure(config_int, weight=1)

        return root

    @staticmethod
    def on_exit(main_window, frame):
        frame.destroy()
        main_window.destroy()

    def set_up(self, board_game, root):
        root.title("Checkers")
        root.geometry('1100x1100-80-100')
        self.config(board_game, root, False)

    def board_replay_render(self, board_ui, frame, main_window, move_index, game_index, max_games):
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

        label_opts = ("Helvetica", 23)
        int_opts = ("Helvetica", 30)

        label_frame = tkinter.LabelFrame(frame, borderwidth=2, relief='solid')
        label_frame.grid(row=0, column=8, rowspan=8, sticky='nsew')

        game_index = "{}/{}".format(str(game_index), str(max_games))
        move_index = "{}".format(str(move_index))

        game_index_label = tkinter.Label(frame, bg='white', text="Game Index", font=label_opts)
        game_index_label.grid(row=2, column=8, sticky='sew', padx=12, pady=1)
        game_index_int = tkinter.Label(frame, bg='white', text=game_index, font=int_opts)
        game_index_int.grid(row=3, column=8, sticky='new', padx=12, pady=1)

        move_index_label = tkinter.Label(frame, bg='white', text="Move Index", font=label_opts)
        move_index_label.grid(row=4, column=8, sticky='sew', padx=12, pady=1)
        move_index_int = tkinter.Label(frame, bg='white', text=move_index, font=int_opts)
        move_index_int.grid(row=5, column=8, sticky='new', padx=12, pady=1)

        exit_btn = tkinter.Button(frame, text="Exit", fg='red', font=(None, 20),
                                  command=lambda win=main_window, frm=frame: self.on_exit(win, frm))
        exit_btn.grid(row=7, column=8, sticky='new', pady=5, padx=12)

    def board_main_render(self, frame, main_window, board_ui, jumped, kings, move_count):
        board_grid = dict()

        def add_box(grid, box_var, i):
            grid[i] = [box_var]

            return grid

        for board_row in range(len(board_ui.keys())):
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

        text_opts = ("Helvetica", 23)

        text_jumped_one = "Jumped: {}".format(str(jumped[2]))
        text_jumped_two = "Jumped: {}".format(str(jumped[1]))
        text_kings_one = "Kings: {}".format(str(kings[1]))
        text_kings_two = "Kings: {}".format(str(kings[2]))
        move_count = "Moves: {}".format(str(move_count))

        label_frame = tkinter.LabelFrame(frame, borderwidth=2, relief='solid')
        label_frame.grid(row=0, column=8, rowspan=8, sticky='nsew')

        one_label = tkinter.Label(frame, bg='white', text=text_jumped_one, font=text_opts)
        one_label.grid(row=1, column=8, sticky='nsew', padx=12, pady=1)

        two_label = tkinter.Label(frame, bg='white', text=text_jumped_two, font=text_opts)
        two_label.grid(row=5, column=8, sticky='nsew', padx=12, pady=1)

        one_king = tkinter.Label(frame, bg='white', text=text_kings_one, font=text_opts)
        one_king.grid(row=2, column=8, sticky='nsew', padx=12, pady=1)

        two_king = tkinter.Label(frame, bg='white', text=text_kings_two, font=text_opts)
        two_king.grid(row=6, column=8, sticky='nsew', padx=12, pady=1)

        move_label = tkinter.Label(frame, bg='white', text=move_count, font=text_opts)
        move_label.grid(row=3, column=8, sticky='nsew', padx=12, pady=1)

        quit_button = tkinter.Button(frame, text="Quit",
                                     command=lambda win=main_window, frm=frame: self.on_exit(win, frm))
        quit_button.grid(row=7, column=8, sticky='ew', padx=10)

        board_grid.update({8: [one_label], 9: [two_label]})
