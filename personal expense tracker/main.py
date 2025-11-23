import expense_manager
import analytics
import file_handler
import validations

def main():
    """
    The main function that runs the Personal Expense Tracker application.
    It handles the main menu loop.
    """
    expenses = file_handler.load_expenses()
    
    print("Welcome to the Personal Expense Tracker!")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. View Expense Analysis (Totals)")
        print("5. Save and Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            new_expense = expense_manager.create_expense()
            expenses.append(new_expense)
            print("Expense added successfully!")
            
        elif choice == '2':
            expense_manager.display_expenses(expenses)
            
        elif choice == '3':
            category = validations.get_valid_category()
            filtered = expense_manager.filter_by_category(expenses, category)
            expense_manager.display_expenses(filtered)
            
        elif choice == '4':
            total = analytics.calculate_total(expenses)
            cat_breakdown = analytics.calculate_category_totals(expenses)
            
            print(f"\nTotal Expenses: ₹{total}")
            print("\nCategory-wise Breakdown:")
            for cat, amount in cat_breakdown.items():
                print(f"  - {cat}: ₹{amount}")
                
        elif choice == '5':
            file_handler.save_expenses(expenses)
            print("Data saved. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()