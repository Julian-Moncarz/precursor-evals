"""Rotating Maze evaluation task for Inspect AI."""

import re
import sys
from pathlib import Path

# Add parent directory to path for imports
parent_dir = str(Path(__file__).parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from inspect_ai import Task, task
from inspect_ai.dataset import Sample, MemoryDataset
from inspect_ai.scorer import Score, Scorer, accuracy, mean, scorer
from inspect_ai.solver import TaskState, generate, use_tools, solver
from inspect_ai.model import ChatMessageUser

from rotating_maze.maze import generate_maze_instance, MazeState
from rotating_maze.tools import create_movement_tools


def create_system_message(variant: str) -> str:
    """Create system message based on variant.

    Args:
        variant: "stationary" or "non_stationary"

    Returns:
        System message string
    """
    base_message = """You are navigating an ASCII maze. Your goal is to reach 'G' starting from 'S'.

Legend:
- S: Your starting position
- P: Your current position
- G: Goal
- #: Wall (cannot pass)
- .: Open path

Available actions: move_up, move_down, move_left, move_right
- These move you relative to the current view

"""

    if variant == "non_stationary":
        base_message += """Note: The maze view may change during navigation. Your actual position doesn't change - only the visual representation. Pay close attention to the maze layout after each move.

"""

    base_message += "Reach the goal as efficiently as possible."

    return base_message


@scorer(metrics=[accuracy(), mean()])
def maze_scorer():
    """Score maze navigation attempts."""

    async def score(state: TaskState, target):
        """Score the maze navigation.

        Args:
            state: Task state
            target: Target (unused)

        Returns:
            Score object
        """
        # Check if agent succeeded
        success = False
        steps_taken = 0

        # Look through all messages to find final tool output
        final_output = ""
        for message in reversed(state.messages):
            if hasattr(message, 'text') and message.text:
                final_output = message.text
                if "Success! Reached the goal" in final_output:
                    success = True
                    # Extract steps from success message
                    match = re.search(r"in (\d+) moves", final_output)
                    if match:
                        steps_taken = int(match.group(1))
                    break
                elif "Max steps" in final_output or "Task failed" in final_output:
                    # Extract steps from failure message
                    match = re.search(r"Steps: (\d+)/", final_output)
                    if match:
                        steps_taken = int(match.group(1))
                    break

        optimal_steps = state.metadata.get("optimal_path_length", 0)

        if success:
            efficiency = optimal_steps / steps_taken if steps_taken > 0 else 0
            return Score(
                value=1.0,
                answer=final_output,
                metadata={
                    "success": True,
                    "steps_taken": steps_taken,
                    "optimal_steps": optimal_steps,
                    "efficiency": efficiency
                }
            )
        else:
            return Score(
                value=0.0,
                answer=final_output,
                metadata={
                    "success": False,
                    "steps_taken": steps_taken,
                    "optimal_steps": optimal_steps,
                    "efficiency": 0.0
                }
            )

    return score


def create_dataset(num_instances: int = 50, variant: str = "stationary") -> MemoryDataset:
    """Create dataset of maze instances.

    Args:
        num_instances: Number of maze instances to generate
        variant: "stationary" or "non_stationary"

    Returns:
        MemoryDataset with maze samples
    """
    samples = []

    for i in range(num_instances):
        # Generate maze instance
        maze_data = generate_maze_instance(size_range=(12, 18), variant=variant)

        # Create the initial prompt
        system_msg = create_system_message(variant)
        initial_view = maze_data["initial_view"]

        input_text = f"{system_msg}\n\nHere is your maze:\n\n{initial_view}"

        # Create sample
        sample = Sample(
            input=[ChatMessageUser(content=input_text)],
            target="SUCCESS",  # Not used for scoring but required
            id=f"maze_{variant}_{i}",
            metadata={
                "maze_id": i,
                "optimal_path_length": maze_data["optimal_path_length"],
                "max_steps": maze_data["max_steps"],
                "variant": variant,
                "start_pos": maze_data["start_pos"],
                "goal_pos": maze_data["goal_pos"],
                "grid": maze_data["grid"]
            }
        )
        samples.append(sample)

    return MemoryDataset(samples)


@solver
def maze_solver():
    """Create a maze solver instance."""

    async def solve(state: TaskState, generate):
        """Custom solver that manages maze state and tools.

        Args:
            state: Current task state
            generate: Generate function

        Returns:
            Updated task state
        """
        # Create MazeState from metadata
        maze_state = MazeState(
            grid=state.metadata["grid"],
            start_pos=tuple(state.metadata["start_pos"]),
            goal_pos=tuple(state.metadata["goal_pos"]),
            optimal_path_length=state.metadata["optimal_path_length"],
            max_steps=state.metadata["max_steps"],
            variant=state.metadata["variant"]
        )

        # Create tools bound to this maze state
        tools = create_movement_tools(maze_state)

        # Set tools in state
        state.tools = tools

        # Use generate with tools until terminal condition
        max_iterations = state.metadata["max_steps"] + 10  # Safety margin
        for _ in range(max_iterations):
            state = await generate(state)

            # Check if terminal condition reached
            if state.messages and len(state.messages) > 0:
                last_message = state.messages[-1]
                if hasattr(last_message, 'text') and last_message.text:
                    if "Success!" in last_message.text or "Task failed" in last_message.text:
                        break

        return state

    return solve


@task
def rotating_maze(variant: str = "stationary", num_instances: int = 50):
    """Rotating Maze evaluation task.

    Tests agent's ability to navigate a maze when the visual representation
    rotates and flips during navigation.

    Args:
        variant: "stationary" (no rotations) or "non_stationary" (rotations every 5 moves)
        num_instances: Number of maze instances to generate

    Returns:
        Task object
    """
    dataset = create_dataset(num_instances=num_instances, variant=variant)

    return Task(
        dataset=dataset,
        solver=[maze_solver()],
        scorer=maze_scorer(),
        max_messages=300,  # Safety limit
    )
