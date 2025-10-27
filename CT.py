import csv
from datetime import datetime

FILE_NAME = "transactions.csv"
FIELDS = ["id", "type", "amount", "category", "date", "description"]

def init_file():
    try:
        with open(FILE_NAME, "x", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
    except FileExistsError:
        pass

def get_new_id():
    try:
        with open(FILE_NAME, newline='') as f:
            reader = csv.DictReader(f)
            ids = [int(row["id"]) for row in reader]
            return max(ids)+1 if ids else 1
    except:
        return 1

def add_transaction():
    t_type = input("Type (income/expense): ").strip().lower()
    if t_type not in ("income", "expense"):
        print("Invalid type.")
        return
    try:
        amount = float(input("Amount: "))
        if amount <= 0:
            raise ValueError
    except:
        print("Invalid amount.")
        return
    category = input("Category: ").strip()
    date = input("Date (YYYY-MM-DD, blank for today): ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    desc = input("Description: ").strip()
    tid = get_new_id()

    with open(FILE_NAME, "a", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writerow({
            "id": tid, "type": t_type, "amount": amount,
            "category": category, "date": date, "description": desc
        })
    print("Transaction added.")

def view_summary():
    income = expense = 0
    try:
        with open(FILE_NAME, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                amt = float(row["amount"])
                if row["type"] == "income":
                    income += amt
                elif row["type"] == "expense":
                    expense += amt
    except:
        pass
    print(f"Total Income: {income}\nTotal Expenses: {expense}\nBalance: {income-expense}")

def main_menu():
    print("\n--- Student Finance Manager ---")
    print("1. Add Transaction")
    print("2. View Summary")
    print("3. Exit")

def main():
    init_file()
    while True:
        main_menu()
        choice = input("Choose (1-3): ").strip()
        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
