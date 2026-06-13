import csv
from collections import defaultdict

class Expense:
    def __init__(self, amount, category, date, description):
        self.amount = float(amount)
        self.category = category
        self.date = date
        self.description = description
    
    def __str__(self):
        return f"{self.date} | {self.category}: ₹{self.amount} - {self.description}"

def save_expenses(expenses, filename='expenses.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Amount', 'Description'])
        for expense in expenses:
            writer.writerow([expense.date, expense.category, expense.amount, expense.description])

def load_expenses(filename='expenses.csv'):
    loaded_expenses = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row: 
                    date, category, amount, description = row
                    loaded_expenses.append(Expense(amount, category, date, description))
    except FileNotFoundError:
        pass 
    return loaded_expenses

def print_summary(expenses):
    if not expenses:
        print("No data available for summary.")
        return
    
    # Calculate total and category breakdown
    total = 0
    category_totals = defaultdict(float)
    
    for expense in expenses:
        total += expense.amount
        category_totals[expense.category] += expense.amount
        
    print("\n--- Expense Summary ---")
    print(f"Total Expenses: ₹{total:.2f}")
    print("\nBy Category:")
    for category, amount in category_totals.items():
        print(f"- {category}: ₹{amount:.2f}")

def main():
    print("Welcome to your Personal Finance Manager!")
    my_expenses = load_expenses()
    
    while True:
        print("\n" + "="*30)
        print("MAIN MENU:")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. View Category Summary")
        print("4. Exit")
        print("="*30)
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            print("\n--- Add a New Expense ---")
            try:
                amount = input("Enter amount: ")
                category = input("Enter category (Food/Transport/Entertainment/Other): ")
                date = input("Enter date (YYYY-MM-DD): ")
                description = input("Enter description: ")
                
                my_expenses.append(Expense(amount, category, date, description))
                save_expenses(my_expenses)
                print("✅ Expense added successfully!")
            except ValueError:
                print("❌ Error: Invalid input.")
                
        elif choice == '2':
            print("\n--- All Expenses ---")
            if my_expenses:
                for item in my_expenses:
                    print(item)
            else:
                print("No expenses found.")
                
        elif choice == '3':
            print_summary(my_expenses)
            
        elif choice == '4':
            print("Saving data and exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()