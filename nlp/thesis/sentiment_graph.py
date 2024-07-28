import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file
DATA_DIR = "./data/"
file_path = DATA_DIR + "sentiment.csv"
df = pd.read_csv(file_path)

# Extract the final row of the dataframe
final_row = df.iloc[-1]

# Prepare data for the bar chart
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
    "Fine-tuning",
    "LoRA (r=8)",
    "LoRA (r=16)",
    "PT (pl=5)",
    "PT (pl=50)",
    "Adapter (rf=64)",
    "Adapter (rf=16)",
    "UniPELT",
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
output_path = "output/sentiment_result.png"
plt.savefig(output_path)
plt.show()
