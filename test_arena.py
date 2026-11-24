from src.models.inner_arena import InnerArena
from src.models.team import Team

# 1. Setup teams and 6x8 inner arena
team_a = Team("Team A")
team_b = Team("Team B")
arena = InnerArena(team_a.name, team_b.name)

# Grab Team A's col-0 marble (starts at 0, 0) and Team B's col-0 marble (starts at 0, 7)
marble_a0 = arena.get_marble_at(0, 0)
marble_b0 = arena.get_marble_at(0, 7)

print("--- 1. Food (1-step) & Drugs (2-step) Movement ---")
print("Food move (0,0 -> 0,1):", arena.move_marble(marble_a0, 0, 1, max_steps=1))
print("Drugs move (0,1 -> 0,3):", arena.move_marble(marble_a0, 0, 3, max_steps=2))
print("Invalid 3-step move:", arena.move_marble(marble_a0, 0, 6, max_steps=2))

print("\n--- 2. Alcohol Freeze Test ---")
marble_a0.apply_alcohol()
print("Move while frozen:", arena.move_marble(marble_a0, 0, 4, max_steps=1))
arena.end_turn_updates(team_a.name)
arena.end_turn_updates(team_a.name)
print("Move after thawing:", arena.move_marble(marble_a0, 0, 4, max_steps=1))

print("\n--- 3. Protein Knockback & Base Score Test ---")
# Move Team B's marble up to (0, 5) right in front of Team A's marble at (0, 4)
arena.move_marble(marble_b0, 0, 5, max_steps=2)
print("Blocked without Protein:", arena.move_marble(marble_a0, 0, 5, max_steps=1))

# Apply Protein and knock Team B's marble back to (0, 7)
marble_a0.apply_protein()
print("Protein knockback (0,4 -> 0,5):", arena.move_marble(marble_a0, 0, 5, max_steps=1))
print("Team B marble respawned at:", (marble_b0.col, marble_b0.row))

# Advance Team A's buffed marble to Team B's back row (row 7) to deal 2 Protein damage
result = arena.move_marble(marble_a0, 0, 7, max_steps=2)
print("Base hit result:", result)
if result["success"] and result["damage"] > 0:
    team_b.base_hp = max(0, team_b.base_hp - result["damage"])

print(f"Team B remaining Base HP: {team_b.base_hp}")
print("Team A scoring marble respawned at:", (marble_a0.col, marble_a0.row))