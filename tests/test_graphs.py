"""Test graph generation with mock data."""

import json
from pathlib import Path

# Create mock log data
log_dir = Path("results/logs")
log_dir.mkdir(parents=True, exist_ok=True)

# Mock results for testing
mock_results = [
    {
        "model": "anthropic/claude-3-5-sonnet-20241022",
        "eval": {
            "task_args": {"variant": "stationary"}
        },
        "results": {
            "scores": [
                {"metadata": {"success": True, "steps_taken": 15, "optimal_steps": 12, "efficiency": 0.8}},
                {"metadata": {"success": True, "steps_taken": 20, "optimal_steps": 15, "efficiency": 0.75}},
                {"metadata": {"success": False, "steps_taken": 50, "optimal_steps": 18, "efficiency": 0.0}},
            ]
        }
    },
    {
        "model": "anthropic/claude-3-5-sonnet-20241022",
        "eval": {
            "task_args": {"variant": "non_stationary"}
        },
        "results": {
            "scores": [
                {"metadata": {"success": True, "steps_taken": 25, "optimal_steps": 12, "efficiency": 0.48}},
                {"metadata": {"success": False, "steps_taken": 50, "optimal_steps": 15, "efficiency": 0.0}},
                {"metadata": {"success": False, "steps_taken": 50, "optimal_steps": 18, "efficiency": 0.0}},
            ]
        }
    },
    {
        "model": "openai/gpt-4o",
        "eval": {
            "task_args": {"variant": "stationary"}
        },
        "results": {
            "scores": [
                {"metadata": {"success": True, "steps_taken": 18, "optimal_steps": 12, "efficiency": 0.67}},
                {"metadata": {"success": True, "steps_taken": 22, "optimal_steps": 15, "efficiency": 0.68}},
                {"metadata": {"success": True, "steps_taken": 25, "optimal_steps": 18, "efficiency": 0.72}},
            ]
        }
    },
    {
        "model": "openai/gpt-4o",
        "eval": {
            "task_args": {"variant": "non_stationary"}
        },
        "results": {
            "scores": [
                {"metadata": {"success": True, "steps_taken": 30, "optimal_steps": 12, "efficiency": 0.4}},
                {"metadata": {"success": False, "steps_taken": 50, "optimal_steps": 15, "efficiency": 0.0}},
                {"metadata": {"success": True, "steps_taken": 35, "optimal_steps": 18, "efficiency": 0.51}},
            ]
        }
    }
]

# Write mock log files
for i, result in enumerate(mock_results):
    log_file = log_dir / f"mock_result_{i}.json"
    with open(log_file, "w") as f:
        json.dump(result, f, indent=2)

print(f"✅ Created {len(mock_results)} mock log files")

# Run graph generation
print("\n📊 Generating graphs from mock data...")
import sys
sys.path.insert(0, "scripts")
import generate_graphs
generate_graphs.main()

print("\n✅ Graph generation complete!")
print("Check results/ directory for:")
print("  - success_rates.png")
print("  - efficiency.png")
print("  - summary.txt")
