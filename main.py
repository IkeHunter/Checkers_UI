import checkers_gui as gui
import tkinter


def main():
    checkers = gui.CheckersGUI()

    main_window = tkinter.Tk()
    main_window.title("Checkers")
    main_window.geometry('900x900-80-100')
    checkers.main_loop(main_window)
    main_window.mainloop()

    # return checkers


if __name__ == '__main__':
    # main_window = tkinter.Tk()
    # main_window.title("Checkers")
    # main_window.geometry('900x900-80-100')
    # main_window.rowconfigure(0, weight=1)
    # main_window.columnconfigure(0, weight=1)
    # some_label = tkinter.Label(main_window, text="hello")
    # some_label.grid(row=0, column=0)
    # # checkers.main_loop(main_window)
    # main_window.mainloop()
    main()
