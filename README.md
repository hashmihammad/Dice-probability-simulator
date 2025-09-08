# Dice Probability Simulator

This project simulates the probability distribution of rolling **two six-sided dice**.  
It calculates the frequency and probability of each possible sum (2–12) and visualizes the distribution using **Matplotlib**.

---

## Features
- Counts how many ways each sum (2–12) can occur.
- Calculates the probability of each outcome.
- Saves results to a CSV file (`dice_probabilities.csv`).
- Visualizes probabilities with a bar chart.

---

## Requirements
Install dependencies before running the script:

```bash
pip install pandas matplotlib
````

---

## Usage

Run the Python script:

```bash
python dice_probabilities.py
```

This will:

1. Print the probability distribution in the terminal.
2. Save the data into a CSV file (`dice_probabilities.csv`).
3. Display a bar chart of the probabilities.

---

## Example Output

| Sum | Count | Probability |
| --- | ----- | ----------- |
| 2   | 1     | 0.0278      |
| 3   | 2     | 0.0556      |
| 4   | 3     | 0.0833      |
| 5   | 4     | 0.1111      |
| 6   | 5     | 0.1389      |
| 7   | 6     | 0.1667      |
| 8   | 5     | 0.1389      |
| 9   | 4     | 0.1111      |
| 10  | 3     | 0.0833      |
| 11  | 2     | 0.0556      |
| 12  | 1     | 0.0278      |

---

## License

This project is licensed under the **MIT License** – you are free to use, modify, and distribute it.

---

## Author

* **Your Name**
* GitHub: [@hashmihammad](https://github.com/hashmihammad)
