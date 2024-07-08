import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file
DATA_DIR = "./data/"
file_path = DATA_DIR + "summarization_eval_rougeL.csv"
df = pd.read_csv(file_path)

# Extract the final row of the dataframe
final_row = df.iloc[-2]

# Prepare data for the bar chart
methods = [
    "Baseline",
    "LoRA-r8",
    "LoRA-r16",
    "PT-pl10",
    "PT-pl20",
    "PT-pl30",
]
rougeL = final_row[
    [f"Group: {method.lower()} - eval/rougeL" for method in methods]
].values
min_rougeL = final_row[
    [f"Group: {method.lower()} - eval/rougeL__MIN" for method in methods]
].values
max_rougeL = final_row[
    [f"Group: {method.lower()} - eval/rougeL__MAX" for method in methods]
].values

# Calculate error bars (difference between overall and min/max)
error_bars = [rougeL - min_rougeL, max_rougeL - rougeL]

# Create the bar chart
plt.figure(figsize=(12, 6))
methods = [
    "Baseline",
    "LoRA-r8",
    "LoRA-r16",
    "PT-pl10",
    "PT-pl20",
    "PT-pl30",
]
bars = plt.bar(
    methods, rougeL, yerr=error_bars, capsize=5, color="dodgerblue", edgecolor="black"
)

# Add labels and title
plt.xlabel("Metode")
plt.ylabel("rougeL Score")
plt.title("ROUGE-L Score Tugas Summarization")
plt.ylim(0.6, 0.8)
plt.grid(axis="y", linestyle="")

# Annotate the bars with the rougeL scores
for bar, err in zip(bars, error_bars[1]):
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        yval + err + 0.001,  # Position text above the error bar
        round(yval, 4),
        ha="center",
        va="bottom",
    )

# Add a dotted line for the baseline threshold
baseline_rougeL = rougeL[0]  # Assuming the first method is baseline
plt.axhline(y=baseline_rougeL, color="r", linestyle="--", linewidth=2)
plt.text(
    len(methods) - 1,
    baseline_rougeL + 0.005,
    f"Baseline: {baseline_rougeL:.4f}",
    color="r",
    ha="center",
)

# Save the plot as a PNG file
output_path = "summarization_eval_rougeL.png"
plt.savefig(output_path)
plt.show()
