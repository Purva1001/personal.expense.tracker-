def calculate_total(expense_list):
    """
    Calculates the sum of all expense amounts.
    """
    total = 0
    for exp in expense_list:
        total += exp['amount']
    return total

def calculate_category_totals(expense_list):
    """
    Calculates the total expense per category.
    Returns a dictionary: {'Food': 500, 'Travel': 200, ...}
    """
    category_totals = {}
    
    for exp in expense_list:
        cat = exp['category']
        amt = exp['amount']
        
        if cat in category_totals:
            category_totals[cat] += amt
        else:
            category_totals[cat] = amt
            
    return category_totals