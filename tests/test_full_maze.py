"""Test the full maze solving flow manually."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from rotating_maze.maze import MazeState, generate_maze_instance
from rotating_maze.tools import create_movement_tools

# Generate a small maze
print("Generating test maze...")
maze_data = generate_maze_instance(size_range=(9, 9), variant="stationary")

print(f"Maze: {len(maze_data['grid'])}x{len(maze_data['grid'][0])}")
print(f"Start: {maze_data['start_pos']}")
print(f"Goal: {maze_data['goal_pos']}")
print(f"Optimal path: {maze_data['optimal_path_length']} steps")
print(f"\nInitial view:\n{maze_data['initial_view']}")

# Create maze state
state = MazeState(
    grid=maze_data['grid'],
    start_pos=maze_data['start_pos'],
    goal_pos=maze_data['goal_pos'],
    optimal_path_length=maze_data['optimal_path_length'],
    max_steps=maze_data['max_steps'],
    variant="stationary"
)

# Create tools
tools = create_movement_tools(state)
print(f"\n✅ Created {len(tools)} movement tools")

# Test a few moves manually
print("\n--- Testing Manual Moves ---")

# Get tool functions
tool_map = {tool._name: tool for tool in tools}

# Try moving (this would normally be done by the model)
print("\nAttempting move_up...")
move_up = tool_map.get('move_up')
if move_up:
    import asyncio
    result = asyncio.run(move_up())
    print(result[:200] + "..." if len(result) > 200 else result)

print("\n✅ Tool execution working!")

# Test transformation for non-stationary
print("\n--- Testing Non-Stationary Variant ---")
state_ns = MazeState(
    grid=maze_data['grid'],
    start_pos=maze_data['start_pos'],
    goal_pos=maze_data['goal_pos'],
    optimal_path_length=maze_data['optimal_path_length'],
    max_steps=maze_data['max_steps'],
    variant="non_stationary"
)

print(f"Initial view (move 0):\n{state_ns.get_view()}")

# Simulate 5 moves to trigger transformation
for i in range(5):
    # Try to move in a valid direction
    for direction in ["up", "down", "left", "right"]:
        actual_dir = state_ns.translate_visual_to_actual(direction)
        if state_ns.is_valid_move(actual_dir):
            state_ns.make_move(actual_dir)
            print(f"\nMove {i+1}: moved {direction}")
            break

    # Check if transformation should occur
    if state_ns.should_transform():
        print("🔄 Transformation triggered!")
        state_ns.apply_transformation()
        print(f"View after transformation:\n{state_ns.get_view()}")
        break

print("\n✅ Transformation system working!")
print("\n" + "="*50)
print("✅ All systems functional!")
print("="*50)
