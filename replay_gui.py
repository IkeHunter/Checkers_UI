import pickle


class InstantReplay():

    def __init__(self):
        pass

    @staticmethod
    def read_move_file():

        def file_read():
            with open('moves.pkl', 'rb') as move_file:
                move_dict = pickle.load(move_file)

            print(move_dict)

        file_read()