import pickle
import tkinter as tk
import time
import json
import copy

import checkers_gui as gui


class InstantReplay:

    def __init__(self):
        self.moves = None
        self.main_window = tk.Tk()
        self.game_gui = gui.CheckersUI(self.main_window)
        self.index = 0

    def read_move_file(self):

        with open('moves') as move_file:
            move_dict = copy.deepcopy(json.load(move_file))

        self.moves = move_dict

        self.game_gui.set_up(self.moves[0], self.main_window)

        print("Moves Unique: {}, Moves Count: {}".format(move_dict[0] != move_dict[1], len(move_dict)))

    def render_moves(self):

        print("Move Index: {}".format(self.index, self.moves[self.index]))
        for key in self.moves[self.index].keys():
            print(self.moves[self.index][key])
        print("\n")

        frame = tk.Frame(self.main_window, bg='systemTransparent')
        frame.grid(row=0, column=0, sticky='nsew', columnspan=8, rowspan=8, padx=0)
        frame = self.game_gui.config(self.moves[0], frame, False)

        self.game_gui.board_render(self.moves[self.index], frame, self.index)

        if self.index < len(self.moves) - 1:
            self.index += 1

            self.main_window.after(250, self.render_moves)

        else:
            print("all done")

    def display_file_contents(self):
        for board in self.moves:

            for key in board.keys():
                print(board[key])
            print('\n')

    def render_complete_board(self):
        self.game_gui.set_up(self.moves[0], self.main_window)
        self.main_window.after(250, self.render_moves)
        self.main_window.mainloop()


replay = InstantReplay()
replay.read_move_file()
replay.render_complete_board()

