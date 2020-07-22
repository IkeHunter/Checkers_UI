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

        self.game_gui.board_render(self.moves[self.game_index][self.move_index], frame, self.move_index, self.game_index, self.max_games)

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

    def render_main_menu(self):
        main_window = tk.Tk()
        main_window.title("Checkers Replay Main Menu")
        main_window.geometry('1100x1100-80-100')

        scframe = VerticalScrolledFrame(main_window)
        scframe.pack()

        for game in range(self.max_games + 1):
            btn = tk.Button(scframe.interior, height=1, width=20, relief=tk.FLAT, text='Game {}'.format(game),
                            command= lambda i=game, win=main_window: self.transfer_to_game(i, win))
            btn.pack(padx=10, pady=5, side=tk.TOP)

        main_window.mainloop()

    def transfer_to_game(self, game, main_window):
        print("Game {} selected".format(game))
        main_window.destroy()
        self.game_index = str(game)
        self.render_game()


replay = InstantReplay()
replay._read_move_file()
# replay.render_game()
replay.render_main_menu()
