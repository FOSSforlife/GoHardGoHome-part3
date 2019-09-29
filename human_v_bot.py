from __future__ import print_function
# tag::play_against_your_bot[]
from dlgo import agent
from dlgo import goboard
from dlgo import gotypes
from get_score import compute_score
from dlgo.utils import print_board, print_move, point_from_coords
from six.moves import input


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
    bot = agent.RandomBot()

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
# end::play_against_your_bot[]

