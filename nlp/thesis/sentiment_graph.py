import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file
DATA_DIR = "./data/"
file_path = DATA_DIR + "sentiment_eval_f1.csv"
df = pd.read_csv(file_path)

# Extract the final row of the dataframe
final_row = df.iloc[-1]

# Prepare data for the bar chart
methods = [
    "Baseline",
    "LoRA-r8",
    "LoRA-r16",
    "PT-pl10",
    "PT-pl20",
    "PT-pl30",
    "UniPELT",
    "Seq_BN",
]
f1 = final_row[[f"Group: {method.lower()} - eval/f1" for method in methods]].values
min_f1 = final_row[
    [f"Group: {method.lower()} - eval/f1__MIN" for method in methods]
].values
max_f1 = final_row[
    [f"Group: {method.lower()} - eval/f1__MAX" for method in methods]
].values

# Calculate error bars (difference between overall and min/max)
error_bars = [f1 - min_f1, max_f1 - f1]

# Create the bar chart
plt.figure(figsize=(12, 6))
methods = [
    "Baseline",
    "LoRA-r8",
    "LoRA-r16",
    "PT-pl10",
    "PT-pl20",
    "PT-pl30",
    "UniPELT",
    "Bottleneck",
]
bars = plt.bar(
    methods, f1, yerr=error_bars, capsize=5, color="dodgerblue", edgecolor="black"
)

# Add labels and title
plt.xlabel("Metode")
plt.ylabel("F1 Score")
plt.title("F1 Score Tugas Sentiment Analysis")
plt.ylim(0.8, 0.9)
plt.grid(axis="y", linestyle="")

# Annotate the bars with the F1 scores
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
baseline_f1 = f1[0]  # Assuming the first method is baseline
plt.axhline(y=baseline_f1, color="r", linestyle="--", linewidth=2)
plt.text(
    len(methods) - 1,
    baseline_f1 + 0.005,
    f"Baseline: {baseline_f1:.4f}",
    color="r",
    ha="center",
)

# Save the plot as a PNG file
output_path = "sentiment_eval_f1.png"
plt.savefig(output_path)
plt.show()
