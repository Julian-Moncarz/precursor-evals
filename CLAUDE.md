# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains **precursor-evals** - a collection of proxy evaluations designed to predict LLM performance on longer-horizon tasks. The project investigates two hypothesized "precursor abilities":
1. **Non-stationarity** - ability to handle changes in the environment (e.g., changing rules, targets, or visual representations)
2. **Stochasticity** - ability to handle randomness and noisy environments

The evaluations are built using the [Inspect AI](https://inspect.ai-safety-institute.org.uk/) framework and aim to predict performance on consequential evals like SWE-bench and Cybench through generalized linear models (GLMs).

## Environment Setup

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install inspect-ai anthropic openai google-generativeai
```

**Key Dependencies:**
- `inspect-ai` - Evaluation framework
- `anthropic` - Anthropic API client
- `openai` - OpenAI API client
- Standard libraries: `numpy`, `matplotlib` (for visualization)

**Environment Variables Required:**
- `ANTHROPIC_API_KEY` - For Claude models
- `OPENAI_API_KEY` - For GPT models
- `GOOGLE_API_KEY` - For Gemini models (optional)

## Running Evaluations

### Basic Command Structure
```bash
# Activate environment first
source venv/bin/activate

# Run a specific eval
inspect eval <path_to_task.py>@<task_name> \
    -T variant=<variant_name> \
    -T num_instances=<number> \
    --model <model_name> \
    --log-dir results/logs
```

### Example: Rotating Maze Eval
```bash
# Stationary variant (baseline)
inspect eval rotating_maze/task.py@rotating_maze \
    -T variant=stationary \
    -T num_instances=50 \
    --model anthropic/claude-3-5-sonnet-20241022

# Non-stationary variant (with view transformations)
inspect eval rotating_maze/task.py@rotating_maze \
    -T variant=non_stationary \
    -T num_instances=50 \
    --model anthropic/claude-3-5-sonnet-20241022

# Multiple models at once
inspect eval rotating_maze/task.py@rotating_maze \
    -T variant=stationary \
    --model openai/gpt-4o,anthropic/claude-3-5-sonnet-20241022
```

### Using Run Scripts
```bash
# Run comprehensive eval across multiple models
./run_rotating_maze.sh
```

## Repository Structure

### High-Level Architecture

The repository follows a modular evaluation structure where each eval is a self-contained package:

```
precursor-evals/
├── rotating_maze/          # Example eval package
│   ├── __init__.py         # Package exports
│   ├── task.py             # Task definition, dataset creation, scorer
│   ├── maze.py             # Domain-specific logic (maze generation, state)
│   ├── tools.py            # Agent tools (move_up, move_down, etc.)
│   └── README.md           # Eval-specific documentation
├── docs/
│   └── plans/              # Design documents for evaluations
├── venv/                   # Python virtual environment
├── project-overveiw.md     # Detailed project specification
└── questions.md            # Research questions and critiques
```

### Eval Package Pattern

Each evaluation follows a consistent structure:

**1. `task.py` - Central orchestration**
- `@task` decorator defines the evaluation
- Creates dataset of test instances
- Defines solver chain (system message → tools → generate)
- Implements custom scorer
- Handles variants (e.g., stationary vs non_stationary)

**2. `[domain].py` - Domain logic** (e.g., `maze.py`)
- State management classes
- Environment generation (e.g., maze generation with recursive backtracking)
- State transformation logic (e.g., rotations, flips)
- Validation and game rules

**3. `tools.py` - Agent actions**
- Inspect AI `@tool` decorators
- Action execution (e.g., `move_up()`, `move_down()`)
- State updates and feedback
- Silent vs explained transformations

**Key Pattern:** Tools access and modify state, then return natural language feedback to the agent about the results of their action.

## Inspect AI Framework Concepts

### Task Definition Pattern
```python
@task
def my_eval(variant: str = "default", num_instances: int = 50):
    """Task parameters come from -T flags in CLI."""
    dataset = create_dataset(variant, num_instances)

    return Task(
        dataset=dataset,
        solver=[
            system_message("..."),
            use_tools([tool1(), tool2()]),
            generate()
        ],
        scorer=custom_scorer(),
        max_messages=200,  # Limit agent turns
    )
```

### Dataset Structure
```python
Sample(
    input="<user-facing task description>",
    target="<expected output or goal marker>",
    metadata={
        "variant": "non_stationary",
        "optimal_path_length": 25,
        "maze_id": 42,
        # ... other eval-specific data
    }
)
```

### Custom Scorers
```python
@scorer(metrics=[accuracy(), mean()])
def my_scorer():
    async def score(state: TaskState, target):
        # Extract information from state.output.completion
        # or state.metadata
        success = check_success_condition(state)

        return Score(
            value=1.0 if success else 0.0,
            metadata={
                "steps_taken": extract_steps(state),
                "efficiency": calculate_efficiency(state),
                # ... other metrics
            }
        )
    return score
```

### Tool Pattern
```python
@tool
def move_up():
    """Docstring becomes tool description for agent."""
    async def execute(state: MazeState):
        # 1. Validate action
        if not state.is_valid_move("up"):
            return "Cannot move up - wall or boundary."

        # 2. Update state
        state.make_move("up")

        # 3. Apply transformations (if variant requires)
        if state.should_transform():
            state.apply_transformation()  # Silent or explained

        # 4. Check completion
        if state.at_goal():
            return f"Success! Reached goal in {state.move_count} moves."

        # 5. Return feedback
        return f"Moved up. Steps: {state.move_count}/{state.max_steps}\n{state.get_view()}"

    return execute
```

## Evaluation Design Principles

### Non-Stationarity Evals
**Core Concept:** Environment changes deterministically during task execution. The agent must adapt to maintain progress toward the goal.

**Variants:**
- **Signposted** - Agent told about changes upfront
- **Unsignposted** - Agent must detect changes from observation
- **Timing** - When changes occur (e.g., every N moves, at halfway point)

**Example Implementations:**
- **Rotating Maze** - Visual representation rotates/flips (state preserved)
- **A-not-B** - Hidden object location switches after N repetitions
- **Tower of Hanoi Target Change** - Goal peg changes mid-task

### Stochasticity Evals
**Core Concept:** Actions have probabilistic outcomes. Agent must be resilient to noise.

**Noise Types:**
- **Valid random move** - Requested action replaced with random valid action
- **No-op** - Action silently ignored
- **Undo** - Previous N actions reversed

**Variants:**
- **Signposted/Unsignposted** - Told about noise probability
- **Explained/Unexplained** - "Lever malfunction" message vs silent failure
- **Noise level** - 10%, 20%, etc.

### Scoring Philosophy
- **Binary success** - Primary metric (1.0 = goal reached, 0.0 = failed)
- **Efficiency** - Secondary metric (optimal_path / actual_path)
- **Max steps** - Typically `optimal_path_length × 3` to allow for errors

## Development Workflow

### Creating a New Eval

1. **Design Phase** - Document in `docs/plans/YYYY-MM-DD-eval-name-design.md`
   - Specify precursor being targeted
   - Define variants
   - Sketch architecture

2. **Implementation**
   ```bash
   mkdir my_eval
   touch my_eval/{__init__.py,task.py,domain.py,tools.py,README.md}
   ```

3. **Core Components** (in order)
   - Domain logic and state management
   - Tool definitions with state updates
   - Dataset generation
   - Task definition with solver chain
   - Custom scorer

4. **Testing**
   ```bash
   # Quick test with small dataset
   inspect eval my_eval/task.py@my_eval -T num_instances=3 --model anthropic/claude-3-5-sonnet-20241022
   ```

5. **Run full evaluation** across models and variants

### Key Implementation Notes

**State Management:**
- Keep state immutable where possible
- Track move count, transformations, optimal path
- Separate "actual coordinates" from "visual representation"

**Transformation Logic (Non-Stationary):**
- Apply transformations to VIEW only, not underlying state
- Provide `translate_visual_to_actual()` methods
- Don't tell agent what transformation occurred (unless variant requires it)

**Tool Feedback:**
- Return natural language descriptions
- Include current view/state representation
- Count moves and check termination conditions
- Provide goal markers (e.g., "Success!" string for scorer to detect)

**Dataset Generation:**
- Generate instances dynamically or pre-generate
- Use `MemoryDataset` for in-memory instances
- Store optimal path length in metadata
- Randomize start/goal positions to avoid positional bias

## Testing

### Unit Testing Pattern
```bash
# Test maze generation
python test_maze.py

# Test individual components
python -m pytest my_eval/
```

### Integration Testing
```bash
# Small run to verify eval works
inspect eval my_eval/task.py@my_eval -T num_instances=3 --model anthropic/claude-3-5-sonnet-20241022

# Check logs
inspect view results/logs/<log_file>.json
```

## Project Context

### Research Goals
This project aims to:
1. Build 8 proxy evals for each precursor (16 total)
2. Achieve construct validity as a cohort
3. Increase precision of predictive GLMs
4. Predict performance on SWE-bench, Cybench, and other consequential evals

### Current Status (see project-overveiw.md for details)
- Stage 2 of multi-stage research project
- Several evals complete: A-not-B, Tower of Hanoi, MAB, Rotating Maze
- Focus on construct validity over any single eval's difficulty

### Key Insight
These are not meant to be individually perfect evaluations. They work as a **cohort** to measure underlying precursor capabilities (adaptability, resilience) that predict general performance.
