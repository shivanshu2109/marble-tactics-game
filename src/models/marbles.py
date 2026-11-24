from src.config import ALCOHOL_FREEZE_TURNS

class Marble:
    def __init__(self, marble_id:int, team_name:str, start_col:int, start_row:int):
        self.marble_id = marble_id
        self.team_name = team_name
        self.start_col = start_col
        self.start_row = start_row
        self.col = start_col  # current X position on the 6-column grid
        self.row = start_row  # current Y position on the 8-row grid
        self.has_protein = False
        self.frozen_turns = 0

    def reset_to_start(self):
        self.col = self.start_col
        self.row = self.start_row
        self.has_protein = False
        
    def apply_protein(self):
        self.has_protein = True

    def apply_alcohol(self):
        self.frozen_turns = ALCOHOL_FREEZE_TURNS
    
    def is_frozen(self) -> bool:
        return self.frozen_turns > 0
    
    def tick_freeze(self):
        if self.frozen_turns > 0:
            self.frozen_turns -= 1

