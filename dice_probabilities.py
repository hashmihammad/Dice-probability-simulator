import pandas as pd
import matplotlib.pyplot as plt

counts = {}
for i in range(2, 13):
    counts[i] = 0

for die1 in range(1, 7):
    for die2 in range(1, 7):
        total = die1 + die2
        counts[total] = counts[total] + 1

total_outcomes = 6 * 6

data = []
for sum_val in range(2, 13):
    prob = counts[sum_val] / total_outcomes
    data.append({"Sum": sum_val, "Count": counts[sum_val], "Probability": prob})

df = pd.DataFrame(data)

print(df)

df.to_csv("dice_probabilities.csv", index=False)

plt.bar(df["Sum"], df["Probability"])
plt.xlabel("Dice Sum")
plt.ylabel("Probability")
plt.title("Probability Distribution of Two Dice (Sum 2–12)")
plt.show()
