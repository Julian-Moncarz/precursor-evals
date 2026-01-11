"""Generate graphs from Rotating Maze eval results."""

import json
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from collections import defaultdict


def load_results(log_dir: str = "results/logs"):
    """Load results from Inspect log files.

    Args:
        log_dir: Directory containing log files

    Returns:
        Dictionary mapping (model, variant) -> results list
    """
    log_path = Path(log_dir)
    if not log_path.exists():
        print(f"❌ Log directory {log_dir} not found")
        return {}

    results = defaultdict(list)

    # Find all JSON log files
    for log_file in log_path.glob("**/*.json"):
        try:
            with open(log_file) as f:
                data = json.load(f)

            # Extract model and variant
            model = data.get("model", "unknown")
            # Clean up model name
            if "/" in model:
                model = model.split("/")[1]

            # Get eval info
            eval_info = data.get("eval", {})
            task_args = eval_info.get("task_args", {})
            variant = task_args.get("variant", "unknown")

            # Get results
            results_data = data.get("results", {})
            scores = results_data.get("scores", [])

            for score in scores:
                metadata = score.get("metadata", {})
                results[(model, variant)].append({
                    "success": metadata.get("success", False),
                    "steps_taken": metadata.get("steps_taken", 0),
                    "optimal_steps": metadata.get("optimal_steps", 0),
                    "efficiency": metadata.get("efficiency", 0.0),
                })

        except Exception as e:
            print(f"⚠️  Error loading {log_file}: {e}")
            continue

    return results


def generate_success_rate_graph(results, output_path="results/success_rates.png"):
    """Generate success rate comparison graph.

    Args:
        results: Results dictionary
        output_path: Output file path
    """
    # Organize data
    data = []
    for (model, variant), scores in results.items():
        success_count = sum(1 for s in scores if s["success"])
        total = len(scores)
        success_rate = success_count / total if total > 0 else 0

        data.append({
            "Model": model,
            "Variant": variant,
            "Success Rate": success_rate * 100,
            "Count": f"{success_count}/{total}"
        })

    df = pd.DataFrame(data)

    # Create grouped bar chart
    fig, ax = plt.subplots(figsize=(12, 6))

    # Get unique models and variants
    models = sorted(df["Model"].unique())
    variants = sorted(df["Variant"].unique())

    x = range(len(models))
    width = 0.35

    # Plot bars for each variant
    for i, variant in enumerate(variants):
        variant_data = df[df["Variant"] == variant]
        variant_data = variant_data.set_index("Model").reindex(models, fill_value=0)

        offset = width * (i - len(variants) / 2 + 0.5)
        bars = ax.bar(
            [xi + offset for xi in x],
            variant_data["Success Rate"],
            width,
            label=variant.replace("_", " ").title()
        )

        # Add value labels on bars
        for j, (bar, count) in enumerate(zip(bars, variant_data["Count"])):
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2.,
                height,
                f'{height:.1f}%\n({count})',
                ha='center',
                va='bottom',
                fontsize=8
            )

    ax.set_xlabel("Model", fontsize=12, fontweight='bold')
    ax.set_ylabel("Success Rate (%)", fontsize=12, fontweight='bold')
    ax.set_title("Rotating Maze: Success Rate by Model and Variant", fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(models, rotation=45, ha='right')
    ax.legend()
    ax.set_ylim(0, 110)
    ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Saved success rate graph to {output_path}")
    plt.close()


def generate_efficiency_graph(results, output_path="results/efficiency.png"):
    """Generate efficiency comparison graph (successful runs only).

    Args:
        results: Results dictionary
        output_path: Output file path
    """
    # Organize data
    data = []
    for (model, variant), scores in results.items():
        successful = [s for s in scores if s["success"]]
        if successful:
            avg_efficiency = sum(s["efficiency"] for s in successful) / len(successful)
            data.append({
                "Model": model,
                "Variant": variant,
                "Avg Efficiency": avg_efficiency * 100,
                "N": len(successful)
            })

    if not data:
        print("⚠️  No successful runs to plot efficiency")
        return

    df = pd.DataFrame(data)

    # Create grouped bar chart
    fig, ax = plt.subplots(figsize=(12, 6))

    models = sorted(df["Model"].unique())
    variants = sorted(df["Variant"].unique())

    x = range(len(models))
    width = 0.35

    for i, variant in enumerate(variants):
        variant_data = df[df["Variant"] == variant]
        variant_data = variant_data.set_index("Model").reindex(models, fill_value=0)

        offset = width * (i - len(variants) / 2 + 0.5)
        bars = ax.bar(
            [xi + offset for xi in x],
            variant_data["Avg Efficiency"],
            width,
            label=variant.replace("_", " ").title()
        )

        # Add value labels on bars
        for bar, n in zip(bars, variant_data["N"]):
            height = bar.get_height()
            if height > 0:
                ax.text(
                    bar.get_x() + bar.get_width() / 2.,
                    height,
                    f'{height:.1f}%\n(n={n})',
                    ha='center',
                    va='bottom',
                    fontsize=8
                )

    ax.set_xlabel("Model", fontsize=12, fontweight='bold')
    ax.set_ylabel("Average Efficiency (%)", fontsize=12, fontweight='bold')
    ax.set_title("Rotating Maze: Path Efficiency (Successful Runs Only)", fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(models, rotation=45, ha='right')
    ax.legend()
    ax.set_ylim(0, 110)
    ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Saved efficiency graph to {output_path}")
    plt.close()


def generate_summary_table(results, output_path="results/summary.txt"):
    """Generate text summary of results.

    Args:
        results: Results dictionary
        output_path: Output file path
    """
    lines = []
    lines.append("=" * 80)
    lines.append("ROTATING MAZE EVALUATION RESULTS")
    lines.append("=" * 80)
    lines.append("")

    for (model, variant), scores in sorted(results.items()):
        lines.append(f"\n{model} - {variant}")
        lines.append("-" * 60)

        total = len(scores)
        success_count = sum(1 for s in scores if s["success"])
        success_rate = success_count / total * 100 if total > 0 else 0

        successful = [s for s in scores if s["success"]]
        if successful:
            avg_steps = sum(s["steps_taken"] for s in successful) / len(successful)
            avg_optimal = sum(s["optimal_steps"] for s in successful) / len(successful)
            avg_efficiency = sum(s["efficiency"] for s in successful) / len(successful) * 100
        else:
            avg_steps = 0
            avg_optimal = 0
            avg_efficiency = 0

        lines.append(f"  Total runs: {total}")
        lines.append(f"  Success rate: {success_rate:.1f}% ({success_count}/{total})")
        if successful:
            lines.append(f"  Avg steps (successful): {avg_steps:.1f}")
            lines.append(f"  Avg optimal path: {avg_optimal:.1f}")
            lines.append(f"  Avg efficiency: {avg_efficiency:.1f}%")

    lines.append("\n" + "=" * 80)

    summary = "\n".join(lines)
    print(summary)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        f.write(summary)

    print(f"\n✅ Saved summary to {output_path}")


def main():
    """Main function to generate all graphs."""
    print("📊 Loading results...")
    results = load_results()

    if not results:
        print("❌ No results found. Run the eval first!")
        return

    print(f"Found results for {len(results)} configurations")

    # Create results directory
    Path("results").mkdir(exist_ok=True)

    # Generate graphs
    generate_success_rate_graph(results)
    generate_efficiency_graph(results)
    generate_summary_table(results)

    print("\n✨ All graphs generated successfully!")


if __name__ == "__main__":
    main()
