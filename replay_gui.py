import tkinter as tk
import json
import copy

import checkers_gui as gui
from scrollable_frame import VerticalScrolledFrame


class InstantReplay:

    def __init__(self):
        self.moves = None
        # self.main_window = tk.Tk()
        self.game_gui = gui.CheckersUI()
        self.move_index = 0
        self.game_index = '0'
        self.max_games = 0

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

    def _render_step(self, main_window, past_frame=None):

        # self._render_terminal_version()

        frame = tk.Frame(main_window, bg='systemTransparent')
        frame.grid(row=0, column=0, sticky='nsew', columnspan=8, rowspan=8, padx=0)
        frame = self.game_gui.config(self.moves[self.game_index][0], frame, False)

        self.game_gui.board_render(self.moves[self.game_index][self.move_index], frame, main_window, self.move_index, self.game_index, self.max_games)

        if past_frame:
            past_frame.grid_forget()

        if self.move_index < len(self.moves[self.game_index]) - 1:
            self.move_index += 1

            main_window.after(150, lambda win=main_window, frm=frame: self._render_step(win, frm))

        else:
            main_window.after(150, lambda win=main_window, frm=frame: self._render_step(win, frm))

    def display_file_contents(self):
        for board in self.moves:

            for key in board.keys():
                print(board[key])
            print('\n')

    def render_game(self):
        main_window = tk.Tk()

        self.game_gui.set_up(self.moves[self.game_index][0], main_window)
        main_window.after(250, lambda win=main_window: self._render_step(win))
        main_window.mainloop()

    @staticmethod
    def _configure_main_menu():
        # Main Configuration
        main_window = tk.Tk()
        main_window.title("Checkers Replay Main Menu")
        main_window.geometry('1100x1100-80-100')

        # Establishing rows and columns on main_window
        main_window.rowconfigure(0, weight=1)
        main_window.rowconfigure(1, weight=1)
        main_window.rowconfigure(2, weight=10)
        main_window.columnconfigure(0, weight=1)
        main_window.columnconfigure(1, weight=3)

        # Setting up containers
        title_container = tk.Frame(main_window, relief=tk.FLAT, bg='light blue')
        title_container.grid(row=0, column=0, sticky='nsew', columnspan=2)

        list_title_container = tk.Frame(main_window)
        list_title_container.grid(row=1, column=0, sticky='nsew')

        list_container = tk.Frame(main_window)
        list_container.grid(row=2, column=0, sticky='nsew')

        # Setting up Labels
        title_label = tk.Label(title_container, text='Checkers Replay Main Menu', font=(None, 40), bg='systemTransparent', fg='white')
        title_label.place(anchor="center", x=550, y=30)

        list_title_label = tk.Label(list_title_container, text='Game Replays', font=(None, 25))
        list_title_label.place(anchor="center", x=275, y=35)

        return main_window, list_container

    def render_main_menu(self):

        main_window, list_container = self._configure_main_menu()

        scframe = VerticalScrolledFrame(list_container)
        scframe.pack(fill=tk.BOTH, expand=1, padx=20, pady=10)

        for game in range(self.max_games + 1):
            btn = tk.Button(scframe.interior, height=3, width=35, relief=tk.FLAT, text='Game {}'.format(game),
                            command= lambda i=game, win=main_window: self.transfer_to_game(i, win))
            btn.pack(padx=10, pady=5, side=tk.TOP, anchor=tk.N)

        main_window.mainloop()

    def transfer_to_game(self, game, main_window):
        print("Game {} selected".format(game))
        # main_window.destroy()
        self.game_index = str(game)

        self.render_game()


replay = InstantReplay()
replay._read_move_file()
# replay.render_game()
replay.render_main_menu()
