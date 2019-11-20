from __future__ import print_function
from dlgo import agent
from dlgo import goboard
from dlgo import gotypes
from get_score import compute_score
from dlgo.utils import print_board, print_move, point_from_coords
from dlgo.agent import load_prediction_agent, load_policy_agent, AlphaGoMCTS
from dlgo.rl import load_value_agent
from six.moves import input
import time
import h5py
import argparse

fast_policy = load_prediction_agent(h5py.File('agents/GHGHbot1_sl_policy.h5', 'r'))
strong_policy = load_policy_agent(h5py.File('agents/GHGHbot1_rl_policy.h5', 'r'))
value = load_value_agent(h5py.File('agents/GHGHbot1_value.h5', 'r'))

alphago = AlphaGoMCTS(strong_policy, fast_policy, value, rollout_limit=10, num_simulations=5)



def main():
    while True:
        board_size = 19
        try:
            board_size = int(board_size)
        except ValueError:
            print('Invalid Entry')
            continue
        if board_size in range(5, 20):
            break
        else:
            print('Invalid Entry')
    game = goboard.GameState.new_game(board_size)
    bot = alphago

    while not game.is_over():
        # print(chr(27) + "[2J")        # We decided not to clear the screen, so we can see the history of the board
        compute_score(game.board)
        print_board(game.board)
        if game.next_player == gotypes.Player.black:
            human_move = input('-- ')
            point = point_from_coords(human_move.strip())
            move = goboard.Move.play(point)
        else:
            move = bot.select_move(game)
        print_move(game.next_player, move)
        game = game.apply_move(move)


if __name__ == '__main__':
    main()
