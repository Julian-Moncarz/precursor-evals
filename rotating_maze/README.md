# Rotating Maze Eval

Tests agent ability to navigate ASCII mazes when the visual representation rotates and flips during navigation.

## Overview

The Rotating Maze evaluation targets the **non-stationarity precursor** - specifically, an agent's ability to handle continuous "view" changes while maintaining task progress. The agent's actual position in the maze doesn't change, only the visual orientation.

## Variants

### Stationary
- No transformations applied
- Tests baseline maze navigation ability

### Non-Stationary
- View transforms every 5 moves
- Random selection from: rotate 90°, rotate 180°, rotate 270°, flip horizontal, flip vertical
- Agent NOT told which transformation occurred
- Must adapt by observing visual changes

## Running the Eval

```bash
# Activate virtual environment
source venv/bin/activate

# Stationary variant
inspect eval rotating_maze/task.py@rotating_maze -T variant=stationary --model anthropic/claude-3-5-sonnet-20241022

# Non-stationary variant
inspect eval rotating_maze/task.py@rotating_maze -T variant=non_stationary --model anthropic/claude-3-5-sonnet-20241022

# Multiple models
inspect eval rotating_maze/task.py@rotating_maze -T variant=stationary --model openai/gpt-4,anthropic/claude-3-5-sonnet-20241022

# Custom number of instances (default 50)
inspect eval rotating_maze/task.py@rotating_maze -T variant=stationary -T num_instances=100 --model anthropic/claude-3-5-sonnet-20241022
```

## Metrics

- **Success Rate**: Percentage of mazes solved within max_steps
- **Average Steps**: Mean steps taken on successful runs
- **Efficiency**: optimal_path_length / actual_steps (1.0 = perfect)

## Design Details

### Maze Generation
- Size: 12x12 to 18x18 (random)
- Algorithm: Recursive backtracking (perfect mazes)
- Start and goal randomly placed
- Guaranteed solvable

### Agent Actions
- `move_up()`: Move up relative to current view
- `move_down()`: Move down relative to current view
- `move_left()`: Move left relative to current view
- `move_right()`: Move right relative to current view

### Scoring
- Binary success (1.0 if goal reached, 0.0 otherwise)
- Max steps = optimal_path_length × 3

## Architecture

```
rotating_maze/
├── __init__.py       # Package exports
├── task.py           # Task definition, dataset, scorer
├── maze.py           # Maze generation and state management
├── tools.py          # Movement tools
└── README.md         # This file
```

## Expected Results

We expect models to show:
- High success rates on stationary variant (baseline navigation)
- Lower success rates on non-stationary variant (adaptation challenge)
- Performance gap indicates strength of non-stationarity precursor ability

This eval contributes to predicting performance on longer-horizon tasks like SWE-bench and Cybench.
