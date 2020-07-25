import checkers_board as cg
import agent_players as ag
import checkers_environment as ce

import tkinter as tk
import json
import time

games_to_play = 30

with open('moves.json', 'w') as file:
    json.dump({}, file)

for i in range(games_to_play):
    main_window = tk.Tk()
    board = cg.CheckersBoard(main_window)
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
        action = random_agent_1.random_move()

        obs, reward, done, info = env.step(action, i)

        move_index += 1

        if done:
            time.sleep(2)
            break

        if not done:
            done = random_agent_2.random_turn()

            move_index += 1

            if done:
                time.sleep(2)
                break
