import validations

def create_expense():
    """
    Interacts with the user to create a new expense dictionary.
    Returns:
        dict: A dictionary containing date, category, amount, and description.
    """
    print("\n--- Add New Expense ---")
    date = validations.get_valid_date()
    category = validations.get_valid_category()
    amount = validations.get_valid_amount()
    description = input("Enter a short description: ")
    
    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    return expense

def display_expenses(expense_list):
    """
    Prints the list of expenses in a readable table format.
    """
    if not expense_list:
        print("\nNo expenses found.")
        return

    print("\n" + "-"*60)
    print(f"{'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description'}")
    print("-"*(60))
    
    for exp in expense_list:
        print(f"{exp['date']:<12} | {exp['category']:<15} | ₹{exp['amount']:<9} | {exp['description']}")
    print("-"*(60))

def filter_by_category(expense_list, category):
    """
    Returns a new list containing only expenses of a specific category.
    """
    filtered_list = []
    for exp in expense_list:
        if exp['category'].lower() == category.lower():
            filtered_list.append(exp)
    return filtered_list