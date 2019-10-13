import h5py
from dlgo.agents.predict import load_prediction_agent
from dlgo.agents.predict import DeepLearningAgent
from dlgo import agent
from dlgo import goboard
from dlgo import gotypes
from dlgo.utils import print_board, print_move
from get_score import compute_score
import time


# print("__name__ = ", __name__)

def main():
    while True:
        board_size = input('Enter the dimensions of the square Go board. (Integer between 5 and 19):')
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
        gotypes.Player.black: load_prediction_agent(h5py.File('cnn_agent.h5')),
        gotypes.Player.white: load_prediction_agent(h5py.File('cnn_agent.h5')),
    }
    while not game.is_over():
        time.sleep(0.3)
        print(chr(27) + "[2J")
        compute_score(game.board)
        print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)
    time.sleep(5)

if __name__ == '__main__':
    main()