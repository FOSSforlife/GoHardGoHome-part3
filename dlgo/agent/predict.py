import numpy as np
from dlgo.agent.base import Agent
from dlgo.agent.helpers import is_point_an_eye
from dlgo import encoders
from dlgo import goboard
from dlgo import kerasutil
__all__ = [
    'DeepLearningAgent',
    'load_prediction_agent',
]


class DeepLearningAgent(Agent):
    def __init__(self, model, encoder, print_probs = False):
        Agent.__init__(self)
        self.model = model
        self.encoder = encoder
        self.print_probs = print_probs

    def predict(self, game_state):
        encoded_state = self.encoder.encode(game_state)
        input_tensor = np.array([encoded_state])
        return self.model.predict(input_tensor)[0]

    def print_probabilities(self, probs):
        COLS = 'ABCDEFGHJKLMNOPQRST'
        probs = list(enumerate(probs)) # adds the indexes to the data structure
        probs = sorted(probs, key=lambda x: float(x[1]), reverse=True)
        for i in range(3):
            move_prob = probs[i]
            point = self.encoder.decode_point_index(move_prob[0])
            move_str = '%s%d' % (COLS[point.col - 1], point.row)
            print("{}: {:.2f}%".format(move_str, move_prob[1] * 100))
            # print(probs)


    def select_move(self, game_state):
        num_moves = self.encoder.board_width * self.encoder.board_height
        move_probs = self.predict(game_state)

        move_probs = move_probs ** 3  
        eps = 1e-6
        move_probs = np.clip(move_probs, eps, 1 - eps)  
        move_probs = move_probs / np.sum(move_probs)  
        if(self.print_probs is True):
            self.print_probabilities(move_probs)

        candidates = np.arange(num_moves)  
        ranked_moves = np.random.choice(
            candidates, num_moves, replace=False, p=move_probs)  
        for point_idx in ranked_moves:
            point = self.encoder.decode_point_index(point_idx)
            if game_state.is_valid_move(goboard.Move.play(point)) and \
                    not is_point_an_eye(game_state.board, point, game_state.next_player):  
                return goboard.Move.play(point)
        return goboard.Move.pass_turn()  

    def serialize(self, h5file):
        h5file.create_group('encoder')
        h5file['encoder'].attrs['name'] = self.encoder.name()
        h5file['encoder'].attrs['board_width'] = self.encoder.board_width
        h5file['encoder'].attrs['board_height'] = self.encoder.board_height
        h5file.create_group('model')
        kerasutil.save_model_to_hdf5_group(self.model, h5file['model'])


def load_prediction_agent(h5file, print_probs = False):
    model = kerasutil.load_model_from_hdf5_group(h5file['model'])
    encoder_name = h5file['encoder'].attrs['name']
    if not isinstance(encoder_name, str):
        encoder_name = encoder_name.decode('ascii')
    board_width = h5file['encoder'].attrs['board_width']
    board_height = h5file['encoder'].attrs['board_height']
    encoder = encoders.get_encoder_by_name(
        encoder_name, (board_width, board_height))
    return DeepLearningAgent(model, encoder, print_probs)
