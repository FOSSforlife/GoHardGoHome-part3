from __future__ import print_function
from dlgo import agent
from dlgo import goboard
from dlgo import gotypes
from get_score import compute_score
from dlgo.utils import print_board, print_move, point_from_coords
from dlgo.agent.predict import DeepLearningAgent, load_prediction_agent
from six.moves import input
import time
import h5py
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--bot-file', help="Path to the h5 file that has the bot. i.e. ./agents/deep_bot.h5", required=True)

args = parser.parse_args()

agent1 = h5py.File(args.bot_file, "r")
bot_1_from_file = load_prediction_agent(agent1)

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
    bot = bot_1_from_file

    while not game.is_over():
        print(chr(27) + "[2J")
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
