from src.config import GRID_COLS, GRID_ROWS, MARBLES_PER_TEAM, BASE_DAMAGE,PROTEIN_DAMAGE
from src.models.marbles import Marble

class InnerArena:

    def __init__(self, team_a_name: str, team_b_name: str):
        self.cols, self.rows = GRID_COLS, GRID_ROWS
        self.team_a_name = team_a_name
        self.team_b_name = team_b_name
        self.marbles = []

        for col in range(MARBLES_PER_TEAM):
            marble_a = Marble(col, team_a_name, col, 0)
            self.marbles.append(marble_a)

            marble_b = Marble(col, team_b_name, col, GRID_ROWS - 1)
            self.marbles.append(marble_b)

    def get_marble_at(self, col:int, row:int):
        for marble in self.marbles:
            if marble.col == col and marble.row == row:
                return marble
        return None
    
    def get_team_marbles(self, team_name: str) -> list:
        return [m for m in self.marbles if m.team_name == team_name ]
    
    def is_valid_coordinate(self, col:int, row:int) ->bool:
        return 0 <= col < self.cols and 0 <= row < self.rows

    def move_marble(self, marble: Marble, target_col: int, target_row: int, max_steps: int) -> dict:

        # 1. Freeze check
        if marble.is_frozen():
            return {
                "success": False,
                "message": "Marble is frozen",
                "damage": 0
            }

        # 2. Bounds check
        if not self.is_valid_coordinate(target_col, target_row):
            return {
                "success": False,
                "message": "Out of bounds",
                "damage": 0
            }

        # 3. Step distance check
        steps = abs(target_col - marble.col) + abs(target_row - marble.row)

        if steps == 0 or steps > max_steps:
            return {
                "success": False,
                "message": "Invalid step distance",
                "damage": 0
            }

        # 4. Collision / Protein knockback check
        occupant = self.get_marble_at(target_col, target_row)

        if occupant is not None:
            if occupant.team_name == marble.team_name:
                return {
                    "success": False,
                    "message": "Blocked by teammate",
                    "damage": 0
                }

            if occupant.team_name != marble.team_name and marble.has_protein:
                occupant.reset_to_start()

            else:
                return {
                    "success": False,
                    "message": "Blocked by enemy (need Protein)",
                    "damage": 0
                }

        # 5. Apply move
        marble.col = target_col
        marble.row = target_row

        # Check whether marble reached enemy base
        scored = (
            (marble.team_name == self.team_a_name and target_row == self.rows - 1)
            or
            (marble.team_name == self.team_b_name and target_row == 0)
        )

        if scored:
            damage = PROTEIN_DAMAGE if marble.has_protein else BASE_DAMAGE

            marble.reset_to_start()

            return {
                "success": True,
                "message": "Scored on enemy base!",
                "damage": damage
            }

        # 6. Normal move
        return {
            "success": True,
            "message": "Moved",
            "damage": 0
            }


    def end_turn_updates(self, team_name: str):
        for marble in self.get_team_marbles(team_name):
            marble.tick_freeze()