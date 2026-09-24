import tkinter as tk
import json

# Store expenses
expenses = []

# Main window
window = tk.Tk()
window.title("Personal Expense Tracker")
window.geometry("500x600")


# Title
title = tk.Label(
    window,
    text="Personal Expense Tracker",
    font=("Arial", 20)
)
title.pack(pady=10)


# Expense name
name_label = tk.Label(window, text="Expense Name")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()


# Amount
amount_label = tk.Label(window, text="Amount")
amount_label.pack()

amount_entry = tk.Entry(window)
amount_entry.pack()


# Expense list
expenses_list = tk.Listbox(window, width=40)
expenses_list.pack(pady=20)


# Total
total_label = tk.Label(window, text="Total: ₹0.00")
total_label.pack(pady=10)


# Add expense function
def add_expense():

    name = name_entry.get()
    amount = amount_entry.get()

    if name == "" or amount == "":
        return

    try:
        amount = float(amount)
    except ValueError:
        return

    expense = (name, amount)
    expenses.append(expense)
    save_expenses()

    expenses_list.insert(
        tk.END,
        f"{name} - ₹{amount:.2f}"
    )

    # Calculate total
    total = sum(expense[1] for expense in expenses)

    total_label.config(
        text=f"Total: ₹{total:.2f}"
    )

    # Clear input boxes
    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

    # Put cursor back in name box
    name_entry.focus()


# Delete expense function
def delete_expense():

    selected = expenses_list.curselection()

    if not selected:
        return

    index = selected[0]

    # Remove from list
    expenses.pop(index)

    # Remove from GUI
    expenses_list.delete(index)

    # Recalculate total
    total = sum(expense[1] for expense in expenses)

    total_label.config(
        text=f"Total: ₹{total:.2f}"
    )    
def save_expenses():

    with open("Expenses.json" ,"w") as file:
        json.dump(expenses,file)



def clear_all():

    expenses.clear()

    expenses_list.delete(0,tk.END)

    total_label.config(text="Total: ₹0.00") 
    
def load_expenses():

    try:
        with open("Expenses.json","r") as file:
            saved_expenses = json.load(file)

        expenses.extend(saved_expenses)

        for expense in expenses:
            expenses_list.insert(
               tk.END,
                f"{expense[0]} -₹{float(expense[1]):.2f}"
            )
            
        total=sum(float(expense[1]) for expense in expenses)

        total_label.config(
        text=f"Total:  ₹(total:.2f)"
    )

    except FileNotFoundError:
        pass     




# Add button
add_button = tk.Button(
    window,
    text="Add Expense",
    command=add_expense
)
add_button.pack(pady=10)


# Delete button
delete_button = tk.Button(
    window,
    text="Delete Expense",
    command=delete_expense
)
delete_button.pack(pady=20)

#Clear all button 
clear_button = tk.Button(
    window,
    text="Clear All",
    command=clear_all

)
clear_button.pack(pady=10)

#Load saved expenses
load_expenses()

# Start application
window.mainloop()