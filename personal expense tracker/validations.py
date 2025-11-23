import datetime

VALID_CATEGORIES = ["Food", "Travel", "Education", "Entertainment", "Bills", "Other"]

def get_valid_date():
    """
    Asks user for date input and validates format (YYYY-MM-DD).
    """
    while True:
        date_str = input("Enter Date (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            print("Invalid format! Please use YYYY-MM-DD.")

def get_valid_amount():
    """
    Asks user for amount and ensures it is a positive number.
    """
    while True:
        try:
            amount = float(input("Enter Amount: "))
            if amount > 0:
                return amount
            print("Amount must be positive.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_valid_category():
    """
    Displays categories and ensures user picks a valid one.
    """
    print("Select Category:", ", ".join(VALID_CATEGORIES))
    while True:
        cat = input("Enter Category: ").title()
        if cat in VALID_CATEGORIES:
            return cat
        print(f"Invalid category. Please choose from: {VALID_CATEGORIES}")