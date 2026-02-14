expenses = []
monthly_budget = 0


def set_budget():
    global monthly_budget
    monthly_budget = float(input("Enter your monthly budget: ₹"))
    print("Budget set successfully!\n")


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category (Food/Travel/Bills/etc): ")

    expenses.append([name, amount, category])
    print("Expense added!\n")


def view_expenses():
    if not expenses:
        print("No expenses yet.\n")
        return

    print("\n--- All Expenses ---")
    for i, exp in enumerate(expenses, 1):
        print(i, exp[0], "-", "₹" + str(exp[1]), "-", exp[2])
    print()


def total_expense():
    total = sum(exp[1] for exp in expenses)
    print("Total Spent: ₹", total)
    print("Remaining Budget: ₹", monthly_budget - total, "\n")


def category_report():
    if not expenses:
        print("No expenses to report.\n")
        return

    report = {}
    for exp in expenses:
        if exp[2] in report:
            report[exp[2]] += exp[1]
        else:
            report[exp[2]] = exp[1]

    print("\n--- Category Report ---")
    for cat, amt in report.items():
        print(cat, ":", "₹" + str(amt))
    print()


def delete_expense():
    view_expenses()
    if not expenses:
        return

    num = int(input("Enter expense number to delete: "))
    if 1 <= num <= len(expenses):
        removed = expenses.pop(num - 1)
        print("Deleted:", removed[0], "\n")
    else:
        print("Invalid number.\n")


while True:
    print("\nWelcome to Expense tracker\n")
    print("1. Set Budget")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. Category Report")
    print("5. Delete Expense")
    print("6. Total & Remaining")
    print("7. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        set_budget()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        view_expenses()
    elif choice == "4":
        category_report()
    elif choice == "5":
        delete_expense()
    elif choice == "6":
        total_expense()
    elif choice == "7":
        print("Exiting tracker. Stay financially disciplined 😎")
        break
    else:
        print("Invalid choice.\n")
