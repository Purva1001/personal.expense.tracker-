import csv
import os

FILENAME = "my_expenses.csv"

def save_expenses(expense_list):
    """
    Saves the list of expenses to a CSV file.
    Uses 'w' mode to overwrite and update the file.
    """
    try:
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["date", "category", "amount", "description"])
            
            for exp in expense_list:
                writer.writerow([exp["date"], exp["category"], exp["amount"], exp["description"]])
    except IOError as e:
        print(f"Error saving data: {e}")

def load_expenses():
    """
    Loads expenses from the CSV file into a list of dictionaries.
    Returns an empty list if the file doesn't exist.
    """
    expenses = []
    if not os.path.exists(FILENAME):
        return expenses

    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['amount'] = float(row['amount'])
                expenses.append(row)
    except IOError as e:
        print(f"Error loading data: {e}")
        
    return expenses