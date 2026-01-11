#!/bin/bash

# Script to run Rotating Maze eval on multiple models

# Load .env file if it exists
if [ -f .env ]; then
    echo "📝 Loading environment variables from .env"
    export $(cat .env | grep -v '^#' | xargs)
else
    echo "⚠️  No .env file found. Copy .env.example to .env and add your API keys."
fi

# Check if API keys are set
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "⚠️  ANTHROPIC_API_KEY not set"
fi

if [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  OPENAI_API_KEY not set"
fi

# Activate venv
source venv/bin/activate

# Create results directory
mkdir -p results

# Models to test
MODELS=(
    "openai/gpt-4o"
)

# Number of instances
NUM_INSTANCES=50

echo "🚀 Running Rotating Maze Eval"
echo "============================"
echo "Models: ${MODELS[@]}"
echo "Instances per variant: $NUM_INSTANCES"
echo ""

# Run stationary variant
for model in "${MODELS[@]}"; do
    echo "📊 Running $model - STATIONARY variant..."
    inspect eval rotating_maze/task.py@rotating_maze \
        -T variant=stationary \
        -T num_instances=$NUM_INSTANCES \
        --model "$model" \
        --log-dir results/logs
done

# Run non-stationary variant
for model in "${MODELS[@]}"; do
    echo "📊 Running $model - NON-STATIONARY variant..."
    inspect eval rotating_maze/task.py@rotating_maze \
        -T variant=non_stationary \
        -T num_instances=$NUM_INSTANCES \
        --model "$model" \
        --log-dir results/logs
done

echo ""
echo "✅ Eval runs complete!"
echo "📈 Generating graphs..."
python scripts/generate_graphs.py

echo ""
echo "✨ All done! Results in results/ directory"
