import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV files
DATA_DIR = "./data/"
file_paths = [DATA_DIR + "nerui.csv", DATA_DIR + "nerugm.csv"]

# Create the figure and subplots
fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# Loop through the datasets
for i, file_path in enumerate(file_paths):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Extract the final row of the dataframe
    final_row = df.iloc[-1]

    # Method names
    methods = [
        "Baseline",
        "LoRA-r8",
        "LoRA-r16",
        "PT-pl5",
        "PT-pl50",
        "Seq_BN-rf64",
        "Seq_BN-rf16",
        "UniPELT",
    ]

    # Prepare data for the bar chart
    overall_f1 = final_row[
        [f"Group: {method.lower()} - eval/overall_f1" for method in methods]
    ].values
    min_f1 = final_row[
        [f"Group: {method.lower()} - eval/overall_f1__MIN" for method in methods]
    ].values
    max_f1 = final_row[
        [f"Group: {method.lower()} - eval/overall_f1__MAX" for method in methods]
    ].values

    # Calculate error bars (difference between overall and min/max)
    error_bars = [overall_f1 - min_f1, max_f1 - overall_f1]

    methods = [
        "Fine-tuning",
        "LoRA (r=8)",
        "LoRA (r=16)",
        "PT (pl=5)",
        "PT (pl=50)",
        "Adapter (rf=64)",
        "Adapter (rf=16)",
        "UniPELT",
    ]

    # Plot the dataset
    bars = axes[i].bar(
        methods,
        overall_f1,
        yerr=error_bars,
        capsize=5,
        color="dodgerblue",
        edgecolor="black",
    )
    axes[i].set_xlabel("Metode")
    axes[i].set_ylabel("F1 Score")
    if i == 0:
        axes[i].set_title(f"F1 Score Tugas NER pada Dataset NERUI")
        axes[i].set_ylim(0.8, 1)
    else:
        axes[i].set_title(f"F1 Score Tugas NER pada Dataset NERUGM")
        axes[i].set_ylim(0.8, 0.9)
    axes[i].grid(axis="y", linestyle="")

    # Annotate the bars with the F1 scores
    for bar, err in zip(bars, error_bars[1]):
        yval = bar.get_height()
        axes[i].text(
            bar.get_x() + bar.get_width() / 2,
            yval + err + 0.001,  # Position text above the error barner_gra
            round(yval, 4),
            ha="center",
            va="bottom",
        )

    # Add a dotted line for the baseline threshold
    baseline_f1 = overall_f1[0]  # Assuming the first method is baseline
    axes[i].axhline(y=baseline_f1, color="r", linestyle="--", linewidth=2)
    axes[i].text(
        len(methods) - 1,
        baseline_f1 + 0.005,
        f"Baseline: {baseline_f1:.4f}",
        color="r",
        ha="center",
    )

# Save the plot as a PNG file
output_path = "output/ner_result.png"
plt.savefig(output_path)
plt.show()
