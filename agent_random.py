import checkers_game as cg
import agent_players as ag
import checkers_environment as ce

import tkinter as tk
import os

"""
- env should be set up
- need to test by printing moves to file and creating a function that reads file and
    displays moves
- need to also set up rewards
"""


main_window = tk.Tk()
board = cg.CheckerBoard(main_window)
env = ce.CheckersBridge(board)

random_agent_1 = ag.RandomAgent(1, board, env)
random_agent_2 = ag.RandomAgent(2, board, env)

games_to_play = 1

os.remove('moves')

for i in range(games_to_play):
    # Reset the env
    obs = env.reset()
    episode_rewards = 0
    done = False
    move_index = 0

    board.print_board()

    while not done:
        env.render()
        action = random_agent_1.random_move()  # choose action randomly
        # if action is None:
        #     done = True

        print("action: {}".format(action))

        obs, reward, done, info = env.step(action, random_agent_1.piece)

        move_index += 1
        print("Move Index: {}".format(move_index))

        # status, agent_status = env.has_won()
        # print("status: {}, agent_status: {}".format(status, agent_status))

        # episode_rewards += reward
        if not done:
            done = random_agent_2.random_turn()

            move_index += 1
            print("Move Index: {}".format(move_index))

    # print(episode_rewards)  # print total rewards when done
