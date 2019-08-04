import checkers_gui as gui
import tkinter


def main():
    checkers = gui.CheckersGUI()

    main_window = tkinter.Tk()
    checkers.main_loop(main_window)
    main_window.mainloop()


if __name__ == '__main__':
    main()
