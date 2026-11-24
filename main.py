import random
from src.models.outer_board import OuterBoard
from src.models.team import Team
from src.config import TILE_PAYOUTS

board = OuterBoard()
team_a = Team("Team A")

for turn in range (1,6):
    dice = random.randint(1,6)
    new_pos , passed_start = board.move_position(
        team_a.outer_position, dice
    )

    team_a.outer_position = new_pos

    if passed_start and new_pos!=0:
        start_bonus = TILE_PAYOUTS["START"][0]
        team_a.add_points(start_bonus)

    reward = board.calculate_reward(new_pos)
    team_a.add_points(reward["points"])

    print(
        f"Turn {turn} | "
        f"Dice: {dice} | "
        f"Position: {new_pos} | "
        f"Tile: {reward['tile_type']} | "
        f"Earned: {reward['points']} | "
        f"Total Points: {team_a.points}"
    )

# Test purchasing an item
purchase_success = team_a.buy_item("FOOD")

print("Purchase successful:", purchase_success)
print("Remaining points:", team_a.points)
print("Updated inventory:", team_a.inventory)

