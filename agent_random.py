import checkers_game as cg
import agent_players as ag
import checkers_environment as ce

import tkinter as tk


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

games_to_play = 2

for i in range(games_to_play):
    # Reset the env
    obs = env.reset()
    episode_rewards = 0
    done = False

    board.print_board()

    while not done:
        # env.render()  # draws frame of the game
        action = random_agent_1.random_move()  # choose action randomly
        # if action is None:
        #     done = True

        # Take a step in the env with the chosen action
        print(action)
        obs, reward, done, info = env.step(action, random_agent_1.piece)
        # print("obs: {}, reward: {}, done: {}, info: {}".format(obs, reward, done, info))
        # episode_rewards += reward
        random_agent_2.random_turn()

    print(episode_rewards)  # print total rewards when done
