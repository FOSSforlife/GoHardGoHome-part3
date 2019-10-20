from dlgo import agent
from dlgo import goboard
from dlgo import gotypes
from dlgo.utils import print_board, print_move
from dlgo.agent.predict import DeepLearningAgent, load_prediction_agent
from get_score import compute_score
import time
import h5py
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--bot-file-1', help="Path to the h5 file that has the bot. i.e. ./agents/deep_bot.h5", required=True)
parser.add_argument('--bot-file-2', help="Path to the h5 file that has the bot. i.e. ./agents/deep_bot.h5", required=True)

args = parser.parse_args()

agent1 = h5py.File(args.bot_file_1, "r")
agent2 = h5py.File(args.bot_file_2, "r")
bot_1_from_file = load_prediction_agent(agent1)
bot_2_from_file = load_prediction_agent(agent2)

# better_bot = load_prediction_agent(h5py.File("./agents/deep_bot_3.h5", "r"))
# print("__name__ = ", __name__)

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
        gotypes.Player.black: bot_1_from_file,
        gotypes.Player.white: bot_2_from_file,
    }
    while not game.is_over():
        time.sleep(0.3)
        print(chr(27) + "[2J")
        compute_score(game.board)
        print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)


if __name__ == '__main__':
    main()
