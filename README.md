# Expense Tracker (Python Console Application)

## Overview

This is a simple command-line based Expense Tracker built using Python.  
It allows users to manage their monthly budget, track expenses, categorize spending, and monitor remaining balance.

The project is designed for beginners to practice:
- Lists
- Functions
- Loops
- Conditional statements
- Basic data handling

---

## Features

1. Set Monthly Budget  
   Define your total monthly spending limit.

2. Add Expense  
   Add an expense with:
   - Name
   - Amount
   - Category

3. View Expenses  
   Display all recorded expenses with index numbers.

4. Category Report  
   View total spending grouped by category.

5. Delete Expense  
   Remove an expense using its index number.

6. Total & Remaining  
   Shows:
   - Total amount spent
   - Remaining budget

7. Exit  
   Close the program safely.

---

## How It Works

- Expenses are stored in a list.
- Each expense is stored as:
  
  [name, amount, category]

- Total is calculated using:
  
  sum(expense[1] for expense in expenses)

- Category report uses a dictionary to group and calculate totals.

---

## How to Run

1. Make sure Python is installed.
2. Save the file as:

   expense_tracker.py

3. Run in terminal:

   python expense_tracker.py

---

## Example Usage

1. Set Budget → 20000  
2. Add Expense → Food, 500, Food  
3. Add Expense → Petrol, 1000, Travel  
4. View Expenses  
5. Check Total & Remaining  

---

## Future Improvements

- Save data to file (persistent storage)
- Add date and time for each expense
- Add warning when budget is exceeded
- Convert to GUI using Tkinter or PyQt
- Convert to Web App using Flask
- Add data visualization using matplotlib

---

## Learning Objectives

This project helps in understanding:
- Data structures (list, dictionary)
- Function modularization
- Basic financial logic
- Program structure and menu-driven systems

---

Author: Aditya
Language: Python 3
Project Type: Beginner Console Application
