import json
from datetime import datetime

BUDGET_FILE = 'budget.json'

def load_data():
    try:
        with open(BUDGET_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'income': [], 'expenses': []}

def save_data(data):
    with open(BUDGET_FILE, 'w') as file:
        json.dump(data, file, indent=4)

data = load_data()

def add_income(amount, source, date):
    income = {
        'amount': amount,
        'source': source,
        'date': date
    }
    data['income'].append(income)
    save_data(data)
    print("Income added successfully.")

def add_expense(amount, category, date):
    expense = {
        'amount': amount,
        'category': category,
        'date': date
    }
    data['expenses'].append(expense)
    save_data(data)
    print("Expense added successfully.")

def view_summary():
    total_income = sum(item['amount'] for item in data['income'])
    total_expenses = sum(item['amount'] for item in data['expenses'])
    balance = total_income - total_expenses
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Balance: {balance}")

def view_details():
    print("Income:")
    for item in data['income']:
        print(f"Amount: {item['amount']}, Source: {item['source']}, Date: {item['date']}")
    print("\nExpenses:")
    for item in data['expenses']:
        print(f"Amount: {item['amount']}, Category: {item['category']}, Date: {item['date']}")

def main():
    while True:
        print("\nBudget Tracker Application")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. View Details")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            amount = float(input("Income amount: "))
            source = input("Income source: ")
            date = input("Date (YYYY-MM-DD): ")
            add_income(amount, source, date)
        elif choice == '2':
            amount = float(input("Expense amount: "))
            category = input("Expense category: ")
            date = input("Date (YYYY-MM-DD): ")
            add_expense(amount, category, date)
        elif choice == '3':
            view_summary()
        elif choice == '4':
            view_details()
        elif choice == '5':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
