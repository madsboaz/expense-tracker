import csv
from datetime import datetime

# vars
expenses = []
categories = ['Food', 'Transportation', 'Utilities', 'Entertainment', 'Other']

def display_menu():
    """main menu"""
    print("\nPersonal Expense Tracker")
    print("1. New expense")
    print("2. View expenses")
    print("3. Generate report")
    print("4. Export - CSV")
    print("5. Exit")

def add_expense():
    """new expense"""
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Please enter a number!")
        return
    
    category = input(f"Enter categoty ({', '.join(categories)}): ")
    if category not in categories:
        print("Not a category. Do again!")
        return
    
    description = input("Description (optional): ")
    date = input("Enter the date (YYYY-MM-DD) or leave blank for today ")
    if date == "":
        date = datetime.today().strftime('%Y-%m-%d')
    else:
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print("Invalid date. Try again idiot")
            return

    expenses.append({
        'amount': amount,
        'category': category,
        'description': description,
        'date': date
    })
    print("Expense added")

def view_expenses():
    """Displays all expenses"""
    if not expenses:
        print("No expenses - yet")
        return

    print("\nRecorded Expenses:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['date']} - {expense['category']} - ${expense['amount']:.2f} - {expense['description']}")

def generate_report():
    """Generates a report"""
    if not expenses:
        print("No expenses.")
        return

    report = {}
    for expense in expenses:
        if expense['category'] in report:
            report[expense['category']] += expense['amount']
        else:
            report[expense['category']] = expense['amount']

    print("\nExpense Report")
    for category, total in report.items():
        print(f"{category}: ${total:.2f}")

def export_to_csv():
    """Exports to CSV file"""
    if not expenses:
        print("No expenses recorded")
        return
    
    filename = input("Enter the filename for the CSV (.csv)")
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['date', 'category', 'amount', 'description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(expenses)
    
    print(f"Expenses exported to {filename} success!")

def main():
    """Loop for the app"""
    print("Program started...")  # confirm app running
    
    while True:
        display_menu()
        choice = input("Choose an option!!!")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            generate_report()
        elif choice == '4':
            export_to_csv()
        elif choice == '5':
            print("Goodbye 😘")
            break
        else:
            print("Try again")

if __name__ == "__main__":
    main()
