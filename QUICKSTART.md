# Rotating Maze Eval - Quick Start

## Setup

1. **Set up API keys** - Copy `.env.example` to `.env` and add your keys:
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```

2. **Activate virtual environment**:
   ```bash
   source venv/bin/activate
   ```

## Running the Eval

### Quick Test (3 instances)
```bash
# Test stationary variant
inspect eval rotating_maze/task.py@rotating_maze \
    -T variant=stationary \
    -T num_instances=3 \
    --model anthropic/claude-3-5-sonnet-20241022

# Test non-stationary variant
inspect eval rotating_maze/task.py@rotating_maze \
    -T variant=non_stationary \
    -T num_instances=3 \
    --model anthropic/claude-3-5-sonnet-20241022
```

### Full Run (All Models, Both Variants)
```bash
./scripts/run_rotating_maze.sh
```

This will:
- Run 50 maze instances per variant
- Test 4 models: Claude Sonnet, Claude Haiku, GPT-4o, GPT-4o Mini
- Both stationary and non-stationary variants
- Save logs to `results/logs/`
- Generate graphs automatically

## Generating Graphs

If you've already run evals and just want to regenerate graphs:
```bash
python scripts/generate_graphs.py
```

This creates:
- `results/success_rates.png` - Success rate comparison
- `results/efficiency.png` - Path efficiency comparison
- `results/summary.txt` - Text summary of results

## Results

Results will be in the `results/` directory:
```
results/
├── logs/              # Inspect log files (JSON)
├── success_rates.png  # Success rate graph
├── efficiency.png     # Efficiency graph
└── summary.txt        # Text summary
```

## Customizing

### Change models
Edit `scripts/run_rotating_maze.sh` and modify the `MODELS` array.

### Change instance count
Edit `NUM_INSTANCES` in `scripts/run_rotating_maze.sh` or use:
```bash
inspect eval rotating_maze/task.py@rotating_maze \
    -T variant=stationary \
    -T num_instances=100 \
    --model your-model-here
```

### View logs in browser
```bash
inspect view
```

## What's Being Measured

- **Stationary**: Baseline maze navigation (no transformations)
- **Non-stationary**: View rotates/flips every 5 moves
  - Tests adaptation to continuous view changes
  - Measures non-stationarity precursor ability

**Metrics:**
- Success rate: % mazes solved
- Efficiency: optimal_path / actual_path (closer to 1.0 = better)
- Steps taken: Number of moves to solve

## Troubleshooting

**Import errors**: Make sure you're in the venv:
```bash
source venv/bin/activate
```

**API key errors**: Set your API keys:
```bash
export ANTHROPIC_API_KEY="..."
export OPENAI_API_KEY="..."
```

**No results to graph**: Run the eval first before generating graphs.
