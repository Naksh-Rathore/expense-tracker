# Expense Tracker (Python)

A simple terminal-based expense tracker written in Python. It allows users to log daily expenses, view all records, visualize trends with matplotlib, and manage their records with ease.

## Features

- Add new expenses with category and notes
- Plot expense trends using a line graph
- Remove the latest expense entry
- View all expenses in a table format
- Automatically stores and updates a CSV file

## Requirements

- Python 3.x
- `pandas`
- `matplotlib`

Install dependencies using pip:

```
pip install pandas matplotlib
```

## CSV File Format

The script reads and writes to a file named `expenses.csv`. If the file doesn't exist, create it with the following columns:

```
date,type,expense,notes
```

Each new expense is appended to this file automatically.

Example:

```
2025-07-20,Groceries,45.25,Bought fruits and vegetables
2025-07-21,Transport,10.00,Bus fare
```

## Usage

Run the script:

```
python expense_tracker.py
```

### Menu Options

```
1. Plot expenses
2. Add expense
3. Remove latest expense
4. View expenses
5. Exit
```

Choose the appropriate option by entering a number (1–5).

### Sample Interaction

```
Enter your choice: 2

Enter the category: Food
Enter the amount: 15.75
Enter any notes: Lunch

Expense added successfully.
```

### Plotting

If expense data exists, selecting option 1 will show a line plot of daily expenses using matplotlib.

## File Structure

- `expense_tracker.py` — Main Python script
- `expenses.csv` — CSV data file for storing expenses
- `README.md` — Project documentation

## Security and Notes

- The script does not include user authentication or encryption.
- Data is stored in plain text in the CSV file.
- Ensure you save backups if using this for serious budgeting.

## License

This project is licensed under the MIT License.
