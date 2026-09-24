expenses = []
while True:
 print("==========================")
 print(" Personal Expense Tracker ")
 print("==========================")

 print("1. Add Expense")
 print("2. View Expenses")
 print("3. View Total")
 print("4. Exit")

 choice=input("Enter your choice: ")

 if choice =="1":
    expense_name=input("What did spend on ? ")

    try:
       amount = float(input("Enter amount : ₹"))
    except ValueError:
       print("Please enter a valid amount!")   
       continue

    expense=[expense_name,amount]
    expenses.append(expense)

    print("Expense added successfully!")
 elif choice =="2":
    print("\nYour Expenses:")

    for expense in expenses:
       print(expense[0] ,"₹",expense[1])

 elif choice=="3":
    total = 0

    for expense in expenses:
       total=total + expense[1]

    print("Total spending : ₹", total)

 elif choice =="4":
    print("Thank you for using Expense Tracker!")
    break