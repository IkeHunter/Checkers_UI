import checkers_game as cg
import agent_players as ag
import checkers_environment as ce

import tkinter as tk
import os
import json
import time

"""
- env should be set up
- need to test by printing moves to file and creating a function that reads file and
    displays moves
- need to also set up rewards
"""

games_to_play = 30

with open('moves.json', 'w') as file:
    json.dump({}, file)

for i in range(games_to_play):
    # Reset the env
    print("\n\n\n\n{0} Game {1} {0}\n\n\n\n".format('*' * 20, i))

    main_window = tk.Tk()
    board = cg.CheckerBoard(main_window)
    env = ce.CheckersBridge(board)

    random_agent_1 = ag.RandomAgent(1, board, env)
    random_agent_2 = ag.RandomAgent(2, board, env)

    time.sleep(3)
    obs = env.reset()
    episode_rewards = 0
    done = False
    move_index = 0

    while True:
        # env.render()
        action = random_agent_1.random_move()  # choose action randomly
        # if action is None:
        #     done = True

        # print("action: {}".format(action))

        obs, reward, done, info = env.step(action, random_agent_1.piece, i)

        move_index += 1
        # print("Move Index: {}, Game Index: {}".format(move_index, i))

        # status, agent_status = env.has_won()
        # print("status: {}, agent_status: {}".format(status, agent_status))

        # episode_rewards += reward

        if done:
            # print("\n\n DONE \n\n")
            time.sleep(2)
            break

        if not done:
            done = random_agent_2.random_turn()

            move_index += 1
            # print("Move Index: {}".format(move_index))

            if done:
                # print("\n\n DONE \n\n")
                time.sleep(2)
                break

    # print(episode_rewards)  # print total rewards when done
