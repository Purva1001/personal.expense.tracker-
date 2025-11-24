# personal.expense.tracker-
A Python-based Command Line Interface (CLI) application designed to help students and individuals track daily expenses, categorize spending, and view financial analytics. Features include data persistence via CSV, category-wise filtering, and input validation.

Overview

The Personal Expense Tracker is a CLI (Command Line Interface) based application developed in Python. It helps users track their daily spending, categorize expenses, and analyze where their money is going. This project was built for the CSE1021 Problem Solving and Programming course.

Features

Add Expenses: Record expenses with date, category, amount, and description.

View Expenses: See a formatted table of all past expenses.

Filter: View expenses specific to categories like Food, Travel, etc.

Analytics: Calculate total spending and see a category-wise breakdown.

Data Persistence: Automatically saves and loads data using a CSV file (my_expenses.csv), so data is not lost when the program closes.

Input Validation: Prevents the user from entering invalid dates or negative amounts.

Technologies Used

Language: Python 3

Concepts: Lists, Dictionaries, Functions, File I/O (CSV), Loops, Conditionals, Exception Handling.

How to Run

Ensure Python is installed on your system.

Download all the project files into one folder.

Open a terminal/command prompt in that folder.

Run the main file:

python main.py


Follow the on-screen menu instructions.

File Structure

main.py: Main program loop.

expense_manager.py: Functions for managing expense data.

file_handler.py: Functions for reading/writing to CSV.

analytics.py: Functions for calculations.

validations.py: Functions for checking user input.
