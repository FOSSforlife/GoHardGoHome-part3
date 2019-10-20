from dlgo.gotypes import Player, Point

KOMI = 7.5
directions = {
    "up": (0,1),
    "down": (0,-1),
    "left": (-1, 0),
    "right": (1, 0)
}
class BoardStats():
    def __init__(self, board_state):
        self.white_territory = 0
        self.black_territory = 0
        self.white_stones = 0
        self.black_stones = 0
        self.neutral_points = []
        self.neutral_count = 0
        for point, point_type in board_state.items():
            if point_type == Player.black:
                self.black_stones += 1
            elif point_type == Player.white:
                self.white_stones += 1
            elif point_type == 'b territory':
                self.black_territory += 1
            elif point_type == 'w territory':
                self.white_territory += 1
            elif point_type == 'neutral':
                self.neutral_count += 1
                self.neutral_points.append(point)

        self.white_score = self.white_stones + self.white_territory + KOMI
        self.black_score = self.black_stones + self.black_territory
    
def compute_score(board):
    board_stats = get_stats(board)

    print ("WHITE: {}  BLACK: {}".format(board_stats.white_score, board_stats.black_score))

def get_stats(board):
    board_state = {}

    for row in range(1, board.num_rows + 1):
        for col in range(1, board.num_cols + 1):
            point = Point(row=row, col=col)
            if point in board_state:
                continue
            stone = board.get(point)
            if stone is not None:
                board_state[point] = stone
            else:
                group, unique_players = get_area(point, board)
                if len(unique_players) == 1:
                    player_color = unique_players.pop()
                    point_type = "b territory" if player_color == Player.black else "w territory"
                else:
                    point_type = "neutral"
                for position in group:
                    board_state[position] = point_type

    board_stats = BoardStats(board_state)
    return board_stats

def get_area(point, board, visited=set()):
    if point in visited:
        return [], set()

    points_list = [point]
    player_color_borders = set()
    visited.add(point)
    current_point = board.get(point)
    for row_dif, col_dif in directions.values():
        next_point = Point(row=point.row + row_dif, col=point.col + col_dif)
        if not board.is_on_grid(next_point):
            continue
        player_color = board.get(next_point)
        if player_color == current_point:
            points, borders = get_area(next_point, board, visited)
            points_list += points
            player_color_borders |= borders
        else:
            player_color_borders.add(player_color)
    return points_list, player_color_borders




