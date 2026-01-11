#!/usr/bin/env python3
"""Throwaway script to generate maze examples."""

from rotating_maze.maze import generate_maze_instance
import json

def main():
    print("Generating maze examples...\n")
    print("=" * 80)

    # Generate a few different sized mazes
    configs = [
        (12, "stationary", "Small Stationary"),
        (16, "stationary", "Medium Stationary"),
        (12, "non_stationary", "Small Non-Stationary"),
    ]

    for size, variant, label in configs:
        print(f"\n{label} Maze (size {size}x{size}):")
        print("-" * 80)

        maze_data = generate_maze_instance(size_range=(size, size), variant=variant)

        print(f"Start position: {maze_data['start_pos']}")
        print(f"Goal position: {maze_data['goal_pos']}")
        print(f"Optimal path length: {maze_data['optimal_path_length']}")
        print(f"Max steps allowed: {maze_data['max_steps']}")
        print(f"Variant: {maze_data['variant']}")
        print(f"\nInitial view:")
        # Replace dots with spaces for readability
        readable_view = maze_data['initial_view'].replace('.', ' ')
        print(readable_view)
        print("\n" + "=" * 80)

    # Also save one maze to JSON for inspection
    print("\n\nSaving a detailed maze to 'maze_example.json'...")
    maze_data = generate_maze_instance(size_range=(12, 12), variant="stationary")

    # Make serializable
    save_data = {
        "grid": maze_data["grid"],
        "start_pos": maze_data["start_pos"],
        "goal_pos": maze_data["goal_pos"],
        "optimal_path_length": maze_data["optimal_path_length"],
        "max_steps": maze_data["max_steps"],
        "variant": maze_data["variant"],
        "initial_view": maze_data["initial_view"]
    }

    with open("maze_example.json", "w") as f:
        json.dump(save_data, f, indent=2)

    print("Done! Check maze_example.json for detailed data.")

if __name__ == "__main__":
    main()
