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
        self.move_index = 0
        self.game_index = '0'
        self.max_games = 0

    def read_move_file(self):

        with open('moves.json') as move_file:
            move_dict = copy.deepcopy(json.load(move_file))

        self.moves = move_dict
        print(self.moves)

        self.game_gui.set_up(self.moves['0'][0], self.main_window)

        self.max_games = len(self.moves) - 1

        print("Moves Unique: {}, Games Count: {}"
              .format(move_dict[self.game_index][0] != move_dict[self.game_index][1], self.max_games))

    def render_moves(self):

        print("Move Index: {}, Game Index: {}, Game Moves: {}".format(self.move_index, self.game_index, len(self.moves[self.game_index])))
        for key in self.moves[self.game_index][self.move_index].keys():
            print(self.moves[self.game_index][self.move_index][key])
        print("\n")

        frame = tk.Frame(self.main_window, bg='systemTransparent')
        frame.grid(row=0, column=0, sticky='nsew', columnspan=8, rowspan=8, padx=0)
        frame = self.game_gui.config(self.moves[self.game_index][0], frame, False)

        self.game_gui.board_render(self.moves[self.game_index][self.move_index], frame, self.move_index, self.game_index, self.max_games)

        if self.move_index < len(self.moves[self.game_index]) - 1:
            self.move_index += 1

            self.main_window.after(150, self.render_moves)

        else:
            if int(self.game_index) < self.max_games:
                self.move_index = 0
                self.game_index = str(int(self.game_index) + 1)
                print("\n{0} Game {1} {0}\n".format('*' * 10, self.game_index))

                for i in range(2000):
                    if i % 2 == 0:
                        print("{} ".format(i), end='')

                self.main_window.destroy()
                self.main_window = tk.Tk()
                self.render_complete_board()

                # self.main_window.after(250, self.render_moves)
            else:
                print('No More Games')
                self.main_window.quit()

    def display_file_contents(self):
        for board in self.moves:

            for key in board.keys():
                print(board[key])
            print('\n')

    def render_complete_board(self):
        self.game_gui.set_up(self.moves[self.game_index][0], self.main_window)
        self.main_window.after(250, self.render_moves)
        self.main_window.mainloop()


replay = InstantReplay()
replay.read_move_file()
replay.render_complete_board()

