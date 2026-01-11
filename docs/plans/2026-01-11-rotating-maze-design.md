# Rotating Maze Eval Design

**Date:** 2026-01-11
**Status:** Approved
**Precursor Targeted:** Non-stationarity (continuous "view" change with state preserved)

## Overview

The Rotating Maze eval tests an agent's ability to navigate an ASCII maze when the visual representation rotates and flips during navigation. The agent's actual position doesn't change - only the visual orientation of the maze changes. This targets the precursor ability to handle continuous view changes while maintaining task progress.

## Design Decisions

### Complexity: Medium
- Maze size: 12x12 to 18x18 (randomly selected)
- 4-6 rotations/flips during typical run
- ~50 maze instances for statistical significance

### Agent Perception: Full Maze View
- Agent sees entire ASCII maze with current position marked
- Isolates view-change adaptation from local navigation complexity
- Simpler to implement and debug

### Transformations: Fixed Intervals
- Non-stationary: Transform every 5 moves
- Stationary: No transformations
- Random selection from: rotate 90°, rotate 180°, rotate 270°, flip horizontal, flip vertical
- Agent NOT told which transformation occurred (must infer from visual)

### Agent Actions: Visual Directions Only
- Four tools: `move_up()`, `move_down()`, `move_left()`, `move_right()`
- Movement relative to current view
- No position query tool - agent must rely on visual adaptation

### Scoring: Binary + Efficiency
- Success = 1.0 if goal reached within max_steps
- Efficiency = optimal_path_length / steps_taken
- Max steps = optimal_path_length × 3

### Variants: Minimal (Ship Fast)
- Stationary (no rotations)
- Non-stationary (rotation every 5 moves)

## Architecture

### File Structure
```
rotating_maze/
  __init__.py
  task.py          # Main @task definition
  maze.py          # Maze generation & state management
  tools.py         # Movement tools
  scorer.py        # Custom scorer
  README.md        # Documentation
```

### Core Components

#### 1. Maze Generator
- Algorithm: Recursive backtracking (generates perfect mazes)
- Start (S) and Goal (G) randomly placed (removes positional bias)
- Stores optimal path length during generation
- Ensures unique solution exists

#### 2. Maze State Manager
```python
class MazeState:
    - original_grid: 2D array (never changes)
    - current_position: (x, y) in original coordinates
    - move_count: int
    - rotation_angle: current accumulated rotation (0, 90, 180, 270)
    - flip_state: (h_flipped, v_flipped)
    - max_steps: int
    - optimal_path_length: int

    Methods:
    - get_view() -> returns transformed ASCII representation
    - apply_transformation() -> rotates/flips based on rules
    - is_valid_move(direction) -> checks walls/bounds
    - make_move(direction) -> updates position, triggers transformations
    - translate_visual_to_actual(direction) -> maps visual to coordinate changes
```

**Transformation Logic:**
- Visual only - agent's coordinate system stays consistent
- Tool returns updated maze view WITHOUT explanation of transformation
- Agent must detect changes from visual differences

#### 3. Movement Tools
Four tools with identical pattern:
```python
@tool
def move_up():
    """Move one step up in the current maze view."""
    async def execute(state: MazeState):
        direction = state.translate_visual_to_actual("up")

        if not state.is_valid_move(direction):
            return f"Cannot move up - wall or boundary. Current view:\n{state.get_view()}"

        state.make_move(direction)

        if state.should_transform():
            state.apply_transformation()  # Silent transformation

        if state.at_goal():
            return f"Success! Reached the goal in {state.move_count} moves.\n{state.get_view()}"

        if state.move_count >= state.max_steps:
            return f"Max steps ({state.max_steps}) reached. Task failed.\n{state.get_view()}"

        return f"Moved up. Steps: {state.move_count}/{state.max_steps}\n{state.get_view()}"
```

#### 4. Task Definition
```python
@task
def rotating_maze(variant="stationary"):
    dataset = load_maze_dataset(variant)  # 50 maze instances

    return Task(
        dataset=dataset,
        solver=[
            system_message("maze_system.txt"),
            use_tools([move_up(), move_down(), move_left(), move_right()]),
            generate()
        ],
        scorer=maze_scorer(),
        max_messages=200,
    )
```

**Dataset Format:**
- `input`: Initial maze view + task instructions
- `metadata`: {maze_id, optimal_path_length, max_steps, variant, start_pos, goal_pos}

**System Message:**
```
You are navigating an ASCII maze. Your goal is to reach 'G' starting from 'S'.

Legend:
- S: Your starting position
- P: Your current position
- G: Goal
- #: Wall (cannot pass)
- .: Open path

Available actions: move_up, move_down, move_left, move_right
- These move you relative to the current view

[IF non_stationary]: Note: The maze view may change during navigation. Your actual position doesn't change - only the visual representation. Pay close attention to the maze layout after each move.

Reach the goal as efficiently as possible.
```

#### 5. Scorer
```python
@scorer(metrics=[accuracy(), avg_steps()])
def maze_scorer():
    async def score(state: TaskState, target):
        success = "Success! Reached the goal" in state.output.completion
        steps_taken = extract_steps_from_output(state.output.completion)
        optimal_steps = state.metadata["optimal_path_length"]

        if success:
            efficiency = optimal_steps / steps_taken
            return Score(
                value=1.0,
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
                metadata={
                    "success": False,
                    "steps_taken": steps_taken,
                    "optimal_steps": optimal_steps,
                    "efficiency": 0.0
                }
            )
```

## Running the Eval

```bash
# Stationary variant
inspect eval rotating_maze.py --model anthropic/claude-3-5-sonnet-20241022 -T variant=stationary

# Non-stationary variant
inspect eval rotating_maze.py --model anthropic/claude-3-5-sonnet-20241022 -T variant=non_stationary

# Multiple models
inspect eval rotating_maze.py --model openai/gpt-4,anthropic/claude-3-5-sonnet-20241022,google/gemini-pro
```

## Metrics to Track

- **Success rate**: % of mazes solved
- **Average steps (on success)**: Efficiency measure
- **Average efficiency**: optimal_steps / actual_steps for successful runs
- **Failure modes**: max_steps vs stuck/invalid moves

## Graphing Results

Simple Python script using matplotlib:
- Bar charts comparing success rates across models
- Separate plots for stationary vs non-stationary variants
- Optional efficiency comparison for successful runs

## Implementation Priority

1. Maze generation and state management
2. Movement tools with transformation logic
3. Task definition and dataset creation
4. Scorer implementation
5. Run on models and generate graphs

KISS principle: Ship fast with minimal variants, add complexity later if valuable.
