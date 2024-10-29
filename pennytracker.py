import sqlite3
from datetime import datetime

# Connect to the database (creates the DB if it doesn't exist)
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    description TEXT
)
''')
conn.commit()

def add_expense(date, category, amount, description=""):
    cursor.execute(
        "INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
        (date, category, amount, description)
    )
    conn.commit()
    print("Expense added successfully!")

def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    records = cursor.fetchall()
    print("ID | Date | Category | Amount | Description")
    print("-" * 40)
    for row in records:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")

def delete_expense(expense_id):
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    print("Expense deleted successfully!")

def total_expense_by_category(category):
    cursor.execute(
        "SELECT SUM(amount) FROM expenses WHERE category = ?", (category,)
    )
    total = cursor.fetchone()[0]
    if total:
        print(f"Total expense for {category}: {total}")
    else:
        print(f"No expenses found for category: {category}")

def main():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Total Expense by Category")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description (optional): ")
            add_expense(date, category, amount, description)

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            expense_id = int(input("Enter the expense ID to delete: "))
            delete_expense(expense_id)

        elif choice == '4':
            category = input("Enter category: ")
            total_expense_by_category(category)

        elif choice == '5':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
conn.close()
