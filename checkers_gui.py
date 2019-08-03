import tkinter


class CheckersGUI:

    def __init__(self):
        # self.mainWindow = tkinter.Tk()
        # self.mainWindow.title("Checkers")
        # self.mainWindow.geometry('900x900-80-100')
        self.board = CheckerBoard()
        # self.config()
        # self.board_setup()
        # self.mainWindow.mainloop()

    def config(self, main_window):
        board_obj = self.board.get_board()
        for board_row in range(len(board_obj.keys())):
            main_window.rowconfigure(board_row, weight=1)
            for board_col in range(len(board_obj[board_row])):
                main_window.columnconfigure(board_col, weight=1)

    def board_setup(self, main_window):
        self.board = self.board.start_board()
        board_grid = dict()

        def add_box(grid, box_var, i):  # i=board_row, j=board_col
            if grid[i] == 0:
                grid = [box_var]
            else:
                grid.append(box_var)
            return grid

        for board_row in range(len(self.board.keys())):
            print(board_grid)
            board_grid.update({board_row: 0})
            for board_col in range(len(self.board[board_row])):
                if self.board[board_row][board_col] == 5:
                    box = tkinter.LabelFrame(main_window, padx=5, pady=5, bg='black')\
                        .grid(row=board_row, column=board_col)
                    # if board_grid[board_row].get() is None:
                    #     board_grid[board_row] = [box]
                    # else:
                    #     board_grid[board_row].append(box)
                    board_grid = add_box(board_grid, box, board_row)
                elif self.board[board_row][board_col] == 0:
                    box = tkinter.LabelFrame(main_window, padx=5, pady=5, bg='white')\
                        .grid(row=board_row, column=board_col)
                    board_grid = add_box(board_grid, box, board_row)
                elif self.board[board_row][board_col] == 1:
                    box = tkinter.LabelFrame(main_window, padx=5, pady=5, bg='white', text='O')\
                        .grid(row=board_row, column=board_col)
                    board_grid = add_box(board_grid, box, board_row)

    def main_loop(self, main_window):
        main_window.title("Checkers")
        main_window.geometry('900x900-80-100')
        self.config(main_window)
        self.board_setup(main_window)
        # main_window.mainloop()



class CheckerBoard:

    def __init__(self):

        self.board_dict = {  # 0 = can move to space, 5 = cannot move to space
            0: [5, 0, 5, 0, 5, 0, 5, 0],
            1: [0, 5, 0, 5, 0, 5, 0, 5],
            2: [5, 0, 5, 0, 5, 0, 5, 0],
            3: [0, 5, 0, 5, 0, 5, 0, 5],
            4: [5, 0, 5, 0, 5, 0, 5, 0],
            5: [0, 5, 0, 5, 0, 5, 0, 5],
            6: [5, 0, 5, 0, 5, 0, 5, 0],
            7: [0, 5, 0, 5, 0, 5, 0, 5]
        }
        self.start_board()

    def get_board(self):
        return self.board_dict

    def start_board(self):
        for i in range(len(self.board_dict.keys())):
            if i <= 2 or i >= 5:
                for j in range(len(self.board_dict[i])):
                    if self.board_dict[i][j] == 0:
                        self.board_dict[i][j] = 1
        return self.board_dict

    def print_board(self):
        for i in range(len(self.board_dict.keys())):
            print(self.board_dict[i])
