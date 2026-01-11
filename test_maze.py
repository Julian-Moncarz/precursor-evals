"""Quick test script for maze generation."""

from rotating_maze.maze import generate_maze_instance

# Test maze generation
print("Testing maze generation...")
maze_data = generate_maze_instance(size_range=(12, 12), variant="stationary")

print(f"\nMaze size: {len(maze_data['grid'])}x{len(maze_data['grid'][0])}")
print(f"Start: {maze_data['start_pos']}")
print(f"Goal: {maze_data['goal_pos']}")
print(f"Optimal path length: {maze_data['optimal_path_length']}")
print(f"Max steps: {maze_data['max_steps']}")
print(f"\nInitial view:\n{maze_data['initial_view']}")

print("\n✅ Maze generation working!")
