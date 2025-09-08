import tkinter as tk
from tkinter import simpledialog , messagebox

# Initialize main window
root = tk.Tk()
root.title("ATM Simulator")
root.geometry("400x300")

# Global variables for balance and transactions
Balance = 5000
transactions = []

# Functions for ATM operations
def deposit():
    global Balance
    amount = simpledialog.askinteger("Deposit", "Enter amount to deposit:")
    if amount and amount > 0:
        Balance += amount
        transactions.append(f"Deposited: {amount}")
        messagebox.showinfo("Deposit Successful", f"Updated Balance: {Balance}")
    else:
        messagebox.showwarning("Invalid Input", "Enter a positive amount!")

def withdraw():
    global Balance
    amount = simpledialog.askinteger("Withdraw", "Enter amount to withdraw:")
    if amount and amount > 0:
        if amount <= Balance:
            Balance -= amount
            transactions.append(f"Withdrew: {amount}")
            messagebox.showinfo("Withdrawal Successful", f"Updated Balance: {Balance}")
        else:
            messagebox.showwarning("Insufficient Balance", f"Your balance is only {Balance}")
    else:
        messagebox.showwarning("Invalid Input", "Enter a positive amount!")

def mini_statement():
    if not transactions:
        messagebox.showinfo("Mini Statement", "No transactions yet.")
    else:
        statement = "\n".join(transactions) + f"\nCurrent Balance: {Balance}"
        messagebox.showinfo("Mini Statement", statement)

def exit_atm():
    messagebox.showinfo("Exit", "Thank you for using the ATM!")
    root.destroy()

# Create Buttons for the ATM operations
tk.Button(root, text="Deposit", width=20, command=deposit).pack(pady=10)
tk.Button(root, text="Withdraw", width=20, command=withdraw).pack(pady=10)
tk.Button(root, text="Mini Statement", width=20, command=mini_statement).pack(pady=10)
tk.Button(root, text="Exit", width=20, command=exit_atm).pack(pady=10)

# Run the GUI loop
root.mainloop()