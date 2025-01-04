from matplotlib.dviread import Page
import pandas as pd
import os

# 定義欄位
columns = ['Date', 'Category', 'Amount', 'Type']
data_file = "expense_tracker.csv"

# 資料表
if os.path.exists(data_file):
    transactions = pd.read_csv(data_file)
else:
    transactions = pd.DataFrame(columns=columns)

# 新增交易
def add_transaction():
    global transactions
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Transport): ")
    amount = float(input("Enter amount: "))
    t_type = input("Enter type (Income/Expense): ").capitalize()
    new_transaction = {'Date': date, 'Category': category, 'Amount': amount, 'Type': t_type}
    transactions = pd.concat([transactions, pd.DataFrame([new_transaction])], ignore_index=True)
    print("Transaction added successfully!")

# 編輯交易
def edit_transaction():
    global transactions
    view_transactions()
    try:
        user_input = input("Enter the transaction number to edit: ")
        if not user_input.isdigit():
            raise ValueError("Invalid input. Please enter a valid number.")
        
        index = int(user_input) - 1
        if 0 <= index < len(transactions):
            print("Leave a field empty to keep the current value.")
            date = input(f"Enter new date (current: {transactions.loc[index, 'Date']}): ") or transactions.loc[index, 'Date']
            category = input(f"Enter new category (current: {transactions.loc[index, 'Category']}): ") or transactions.loc[index, 'Category']
            amount = input(f"Enter new amount (current: {transactions.loc[index, 'Amount']}): ")
            t_type = input(f"Enter new type (current: {transactions.loc[index, 'Type']}): ") or transactions.loc[index, 'Type']

            transactions.at[index, 'Date'] = date
            transactions.at[index, 'Category'] = category
            transactions.at[index, 'Amount'] = float(amount) if amount else transactions.loc[index, 'Amount']
            transactions.at[index, 'Type'] = t_type
            print("Transaction updated successfully!")
        else:
            print("Invalid transaction number. Please choose a valid number.")
    except ValueError as e:
        print(e)

# 刪除交易
def delete_transaction():
    global transactions
    view_transactions()
    try:
        user_input = input("Enter the transaction number to delete: ")
        if not user_input.isdigit():
            raise ValueError("Invalid input. Please enter a valid number.")
        
        index = int(user_input) - 1
        if 0 <= index < len(transactions):
            transactions = transactions.drop(index).reset_index(drop=True)
            print("Transaction deleted successfully!")
        else:
            print("Invalid transaction number.")
    except ValueError as e:
        print(e)

def view_transactions():
    if transactions.empty:
        print("No transactions found.")
    else:
        display_data = transactions.copy()
        display_data.index = display_data.index + 1
        print(display_data)

# 查看摘要
def summarize_transactions():
    if transactions.empty:
        print("No transactions found.")
    else:
        summary = transactions.groupby(['Category', 'Type'])['Amount'].sum().reset_index()
        print(summary)

# 儲存並退出
def save_and_exit():
    transactions.to_csv(data_file, index=False)
    print("Data saved. Exiting program.")
    exit()

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Transaction")
        print("2. Edit Transaction")
        print("3. Delete Transaction")
        print("4. View Summary")
        print("5. Save and Exit")
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_transaction()
        elif choice == '2':
            edit_transaction()
        elif choice == '3':
            delete_transaction()
        elif choice == '4':
            summarize_transactions()
        elif choice == '5':
            save_and_exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
