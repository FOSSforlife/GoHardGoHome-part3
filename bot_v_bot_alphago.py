from dlgo import agent
from dlgo import goboard
from dlgo import gotypes
from dlgo.utils import print_board, print_move
from dlgo.agent import load_prediction_agent, load_policy_agent, AlphaGoMCTS
from dlgo.rl import load_value_agent
from get_score import compute_score
import time
import h5py
import argparse

fast_policy = load_prediction_agent(h5py.File('agents/GHGHbot1_sl_policy.h5', 'r'))
strong_policy = load_policy_agent(h5py.File('agents/GHGHbot1_rl_policy.h5', 'r'))
value = load_value_agent(h5py.File('agents/GHGHbot1_value.h5', 'r'))

alphago = AlphaGoMCTS(strong_policy, fast_policy, value)

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
    bots = {
        gotypes.Player.black: alphago,
        gotypes.Player.white: alphago,
    }
    while not game.is_over():
        time.sleep(0.6)
        # print(chr(27) + "[2J")        # We decided not to clear the screen, so we can see the history of the board
        compute_score(game.board)
        print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)


if __name__ == '__main__':
    main()
