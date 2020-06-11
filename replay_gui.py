import pickle
import tkinter as tk
import time
import json

import checkers_gui as gui


class InstantReplay:

    def __init__(self):
        self.moves = None
        self.main_window = tk.Tk()
        self.game_gui = gui.CheckersUI(self.main_window)
        self.index = 0

    def read_move_file(self):

        with open('moves') as move_file:
            move_dict = json.load(move_file)

        self.moves = move_dict

        self.game_gui.set_up(self.moves[0])

        print(move_dict)

        print(move_dict[0] == move_dict[1])

    def render_moves(self):

        # def config_board():
        #     for move in self.moves:
        #         self.main_window.after(1000, self.game_gui.board_render(move))

        # self.main_window.after(100, config_board())
        # self.main_window.mainloop()

        # for move in self.moves:
        #     self.game_gui.board_render(move)
        #     self.main_window.update_idletasks()
        #     self.main_window.update()
        #     time.sleep(1000)

        def iter_one():
            print("index: {}, \nboard: {}".format(self.index, self.moves[self.index]))
            self.game_gui.board_render(self.moves[self.index])
            if self.index < len(self.moves) - 1:
                self.index += 1
                self.main_window.after(500, iter_two())

            else:
                print("all done")

        def iter_two():
            print("index: {}, \nboard: {}".format(self.index, self.moves[self.index]))
            self.game_gui.board_render(self.moves[self.index])
            if self.index < len(self.moves) - 1:
                self.index += 1
                self.main_window.after(500, iter_one())

            else:
                print("all done")

        iter_one()

    def display_file_contents(self):
        for board in self.moves:

            for key in board.keys():
                print(board[key])
            print('\n')



replay = InstantReplay()
replay.read_move_file()
# replay.game_gui.set_up(replay.moves[0])
# replay.main_window.after(500, replay.render_moves())
# replay.main_window.mainloop()
