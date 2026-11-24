import random
from src.models.outer_board import OuterBoard
from src.models.inner_arena import InnerArena
from src.models.team import Team
from src.config import TILE_PAYOUTS


class GameState:
    def __init__(self, team_a_name: str = "Team A", team_b_name: str = "Team B"):
        self.outer_board = OuterBoard()
        self.teams = [Team(team_a_name), Team(team_b_name)]
        self.arena = InnerArena(team_a_name, team_b_name)
        self.current_team_idx = 0
        self.phase = "ROLL" 
        self.last_roll = 0
        self.selected_marble = None
        self.status_message = f"{team_a_name}'s turn - Click Roll Dice!"
        self.winner = None
    
    @property
    def current_team(self) -> Team:
        return self.teams[self.current_team_idx]
    
    @property
    def opponent_team(self) -> Team:
        return self.teams[1 - self.current_team_idx]