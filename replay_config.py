import tkinter as tk
import json
import copy

from checkers_ui import CheckersUI
from scrollable_frame import VerticalScrolledFrame


class GameReplay:

    def __init__(self):
        self.moves = None
        self.move_index = 0
        self.game_index = '0'
        self.max_games = 0
        self.interval = 500

        self._read_move_file()

    def _read_move_file(self):

        with open('moves.json') as move_file:
            move_dict = copy.deepcopy(json.load(move_file))

        self.moves = move_dict
        self.max_games = len(self.moves) - 1

        print("Moves Unique: {}, Games Count: {}"
              .format(move_dict[self.game_index][0] != move_dict[self.game_index][1], self.max_games))

    def _render_terminal_version(self):
        print("Move Index: {}, Game Index: {}, Game Moves: {}"
              .format(self.move_index, self.game_index, len(self.moves[self.game_index])))
        for key in self.moves[self.game_index][self.move_index].keys():
            print(self.moves[self.game_index][self.move_index][key])
        print("\n")

    def _render_step(self, main_window, game_gui, past_frame=None):
        frame = tk.Frame(main_window, bg='systemTransparent')
        frame.grid(row=0, column=0, sticky='nsew', columnspan=8, rowspan=8, padx=0)
        frame = game_gui.config(self.moves[self.game_index][0], frame, False)

        game_gui.board_replay_render(self.moves[self.game_index][self.move_index], frame,
                                     main_window, self.move_index, self.game_index, self.max_games)

        if past_frame:
            past_frame.grid_forget()

        if self.move_index < len(self.moves[self.game_index]) - 1:
            self.move_index += 1

            main_window.after(self.interval, lambda win=main_window, frm=frame, g=game_gui:
                              self._render_step(win, past_frame=frm, game_gui=g))

        else:
            main_window.after(self.interval, lambda win=main_window, frm=frame, g=game_gui:
                              self._render_step(win, past_frame=frm, game_gui=g))

    def display_file_contents(self):
        for board in self.moves:

            for key in board.keys():
                print(board[key])
            print('\n')

    def render_game(self):
        main_window = tk.Tk()

        game_gui = CheckersUI()
        game_gui.set_up(self.moves[self.game_index][0], main_window)
        main_window.after(0, lambda win=main_window, g=game_gui: self._render_step(win, game_gui=g))
        main_window.mainloop()

    def _configure_main_menu(self):
        # Main Configuration
        main_window = tk.Tk()
        main_window.title("Checkers Replay Main Menu")
        main_window.geometry('1100x1100-80-100')

        # Establishing rows and columns on main_window
        main_window.rowconfigure(0, weight=1)
        main_window.rowconfigure(1, weight=1)
        main_window.rowconfigure(2, weight=10)
        main_window.rowconfigure(3, weight=1)
        main_window.columnconfigure(0, weight=1)
        main_window.columnconfigure(1, weight=3)
        main_window.columnconfigure(2, weight=1)

        # Setting up containers
        title_container = tk.Frame(main_window, relief=tk.FLAT, bg='light blue')
        title_container.grid(row=0, column=0, sticky='nsew', columnspan=3)

        list_title_container = tk.Frame(main_window)
        list_title_container.grid(row=1, column=0, sticky='nsew')

        list_container = tk.Frame(main_window)
        list_container.grid(row=2, column=0, sticky='nsew', rowspan=2)

        exit_button_container = tk.Frame(main_window)
        exit_button_container.grid(row=3, column=2, sticky='nsew', padx=5, pady=10)

        # Setting up Labels and Buttons
        title_label = tk.Label(title_container, text='Checkers Replay Main Menu',
                               font=(None, 40), bg='systemTransparent', fg='white')
        title_label.place(anchor="center", x=550, y=25)

        list_title_label = tk.Label(list_title_container, text='Game Replays', font=(None, 25))
        list_title_label.place(anchor="center", x=275, y=35)

        quit_button = tk.Button(exit_button_container, text="Quit", height=2, width=9, fg='red', font=(None, 20),
                                relief=tk.FLAT, command=lambda win=main_window: self._quit_program(win))
        quit_button.pack(side=tk.BOTTOM)

        return main_window, list_container

    @staticmethod
    def _quit_program(main_window):
        main_window.destroy()

    def render_main_menu(self):

        main_window, list_container = self._configure_main_menu()

        scframe = VerticalScrolledFrame(list_container)
        scframe.pack(fill=tk.BOTH, expand=1, padx=20, pady=10)

        for game in range(self.max_games + 1):
            btn = tk.Button(scframe.interior, height=3, width=35, relief=tk.FLAT, text='Game {}'.format(game),
                            command=lambda i=game: self._transfer_to_game(i))
            btn.pack(padx=10, pady=5, side=tk.TOP, anchor=tk.N)

        main_window.mainloop()

    def _transfer_to_game(self, game):
        self.game_index = str(game)
        self.move_index = 0

        self.render_game()
