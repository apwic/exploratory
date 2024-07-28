import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use("seaborn-v0_8-colorblind")

# Load the CSV files
DATA_DIR = "./data/"
file_rougeL = DATA_DIR + "summarization_rougeL.csv"
file_rouge1 = DATA_DIR + "summarization_rouge1.csv"
file_rouge2 = DATA_DIR + "summarization_rouge2.csv"

df_rougeL = pd.read_csv(file_rougeL)
df_rouge1 = pd.read_csv(file_rouge1)
df_rouge2 = pd.read_csv(file_rouge2)

# Extract the final row of the dataframes
final_row_rougeL = df_rougeL.iloc[-1]
final_row_rouge1 = df_rouge1.iloc[-1]
final_row_rouge2 = df_rouge2.iloc[-1]

methods = [
    "base",
    "lora-r8",
    "lora-r16",
    "pt-pl5",
    "pt-pl50",
    "seq_bn-rf64",
    "seq_bn-rf16",
    "unipelt",
]

fold = 0
# Prepare data for the bar chart
rougeL = final_row_rougeL[
    [f"indosum-{method}-{fold} - eval/rougeL" for method in methods]
].values
rouge1 = final_row_rouge1[
    [f"indosum-{method}-{fold} - eval/rouge1" for method in methods]
].values
rouge2 = final_row_rouge2[
    [f"indosum-{method}-{fold} - eval/rouge2" for method in methods]
].values

min_rougeL = final_row_rougeL[
    [f"indosum-{method}-{fold} - eval/rougeL__MIN" for method in methods]
].values
min_rouge1 = final_row_rouge1[
    [f"indosum-{method}-{fold} - eval/rouge1__MIN" for method in methods]
].values
min_rouge2 = final_row_rouge2[
    [f"indosum-{method}-{fold} - eval/rouge2__MIN" for method in methods]
].values

max_rougeL = final_row_rougeL[
    [f"indosum-{method}-{fold} - eval/rougeL__MAX" for method in methods]
].values
max_rouge1 = final_row_rouge1[
    [f"indosum-{method}-{fold} - eval/rouge1__MAX" for method in methods]
].values
max_rouge2 = final_row_rouge2[
    [f"indosum-{method}-{fold} - eval/rouge2__MAX" for method in methods]
].values

# Calculate error bars (difference between overall and min/max)
error_bars_rougeL = [rougeL - min_rougeL, max_rougeL - rougeL]
error_bars_rouge1 = [rouge1 - min_rouge1, max_rouge1 - rouge1]
error_bars_rouge2 = [rouge2 - min_rouge2, max_rouge2 - rouge2]

# Create the bar chart
plt.figure(figsize=(16, 8))
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

x = np.arange(len(methods))
width = 0.2

fig, ax = plt.subplots(figsize=(16, 8))
bars1 = ax.bar(
    x - width - 0.05,
    rouge1,
    width,
    capsize=5,
    label="ROUGE-1",
    edgecolor="black",
)
bars2 = ax.bar(
    x,
    rouge2,
    width,
    capsize=5,
    label="ROUGE-2",
    edgecolor="black",
)
bars3 = ax.bar(
    x + width + 0.05,
    rougeL,
    width,
    capsize=5,
    label="ROUGE-L",
    edgecolor="black",
)

# Add labels and title
ax.set_xlabel("Metode")
ax.set_ylabel("ROUGE Scores")
ax.set_title("ROUGE Scores Tugas Summarization")
ax.set_xticks(x)
ax.set_xticklabels(methods)
ax.legend()

# Annotate the bars with the ROUGE scores
for bars, rouge_scores in zip([bars1, bars2, bars3], [rouge1, rouge2, rougeL]):
    for bar, score in zip(bars, rouge_scores):
        yval = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            yval + 0.001,  # Position text above the bar
            round(yval, 4),
            ha="center",
            va="bottom",
        )

# Save the plot as a PNG file
output_path = "output/summarization_result.png"
plt.savefig(output_path)
plt.show()
