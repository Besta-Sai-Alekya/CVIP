import tkinter as tk
from tkinter import messagebox

class ExpenseSharingApp:
    def __init__(s,r):
        s.r = r
        s.r.title("Expense Sharing App")
        s.expenses = {}
        s.users = set()
        s.create_widgets()

    def create_widgets(s):
        tk.Label(s.r, text="User:").grid(row=0, column=0, sticky="w")
        s.user_entry = tk.Entry(s.r)
        s.user_entry.grid(row=0, column=1)
        tk.Label(s.r, text="Amount:").grid(row=1, column=0, sticky="w")
        s.amount = tk.Entry(s.r)
        s.amount.grid(row=1, column=1)
        tk.Button(s.r, text="Add Expense", command=s.add_expense).grid(row=2, column=1, pady=10)
        tk.Label(s.r, text="Expenses:").grid(row=3, column=0, sticky="w")
        s.expense_listbox = tk.Listbox(s.r, width=50, height=10)
        s.expense_listbox.grid(row=4, column=0, columnspan=2)
        tk.Button(s.r, text="Split Bill", command=s.split_bill).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(s.r, text="Clear Entries", command=s.clear_entries).grid(row=6, column=0, columnspan=2, pady=10)

    def clear_entries(x):
        x.expenses = {}
        x.users = set()
        x.expense_listbox.delete(0, tk.END)
        x.user_entry.delete(0, tk.END)
        x.amount.delete(0, tk.END)


    def add_expense(y):
        user = y.user_entry.get()
        amount = y.amount.get()

        if user and amount:
            y.expenses.setdefault(user, 0)
            y.expenses[user] += float(amount)
            y.users.add(user)
            y.expense_listbox.insert(tk.END, f"{user}: Rs. {amount}")
            y.user_entry.delete(0, tk.END)
            y.amount.delete(0, tk.END)
        else:
            messagebox.showerror("Failed", "Please enter both user and amount.")

    def split_bill(n):
        if len(n.users) < 2:
            messagebox.showerror("Failed", "Add expenses for at least two users.")
            return

        total_expense = sum(n.expenses.values())
        per_person_share = total_expense / len(n.users)
        owed_amounts = {user: per_person_share - n.expenses.get(user, 0) for user in n.users}

        result = "Owe Details:\n"
        for debtor, amount in owed_amounts.items():
            for creditor, credit_amount in owed_amounts.items():
                if debtor != creditor and amount > 0 and credit_amount < 0:
                    transfer_amount = min(amount, -credit_amount)
                    result += f"{debtor} owes Rs. {transfer_amount} to {creditor}\n"
                    amount -= transfer_amount
                    owed_amounts[creditor] += transfer_amount

        messagebox.showinfo("Expense Summary", result)


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseSharingApp(root)
    root.mainloop()
