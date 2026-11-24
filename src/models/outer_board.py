import random
from src.config import OUTER_BOARD_SIZE, TILE_PAYOUTS
class OuterBoard:
    def __init__(self):
        self.size = OUTER_BOARD_SIZE
        self.tiles = ["BLANK"] * OUTER_BOARD_SIZE
        self.tiles[0] = "START"

        tile_positions = {
            "GREEN": [2, 4, 5, 8, 12, 15, 16, 18, 21, 22, 27, 28, 31, 32, 36, 39],
            "YELLOW": [3, 7, 14, 17, 26, 29, 34, 38],
            "BLUE": [1, 19, 33],
            "TASK": [6, 13, 25, 37]
       }
        for tile_type, indices in tile_positions.items():
            for index in indices:
                self.tiles[index]= tile_type
    
    def get_tile_type(self, position):
        return self.tiles[position % self.size]
    
    def move_position(self, current_position, steps):
        new_position = (current_position + steps) % self.size
        passed_start = (current_position + steps) >=self.size

        return new_position, passed_start
    
    def calculate_reward(self, position):
        tile_type = self.get_tile_type(position)
        min_pts, max_pts = TILE_PAYOUTS[tile_type]
        points = random.randint(min_pts, max_pts)

        return {
            "tile_type" : tile_type,
            "points": points
        }