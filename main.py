import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

print('\nExpense Tracker\n')

data = pd.read_csv('expenses.csv')

def plot_expenses(data):
    if data.empty:
        print("\nNo expenses to plot.\n")
        return
        
    x = [i for i in range(1, len(data) + 1)]
    y = list(data['expense'])

    plt.plot(x, y, marker='o')
    plt.xlabel('Day Number')
    plt.ylabel('Amount')
    plt.title('Expense Tracker')
    plt.show()

def close():
    plt.close()
    print("\nThanks for using the program. Goodbye!")

def add_expense(data):
    date = dt.datetime.now().strftime('%Y-%m-%d')
    category = input('\nEnter the category: ')

    while True:
        try:
            expense = float(input('Enter the amount: '))

            if expense > 0:
                break
            else:
                print('Invalid amount. Please try again.')

        except ValueError:
            print('Invalid amount. Please try again.')        

    notes = input('Enter any notes: ')        

    new_row = {
        'date': date,
        'type': category,
        'expense': expense,
        'notes': notes
    }

    new_row_df = pd.DataFrame([new_row])
    data = pd.concat([data, new_row_df], ignore_index=True)
    data.to_csv('expenses.csv', index=False)

    print("\nExpense added successfully.\n")

    return data

def remove_expense(data):
    if not data.empty:
        data = data.drop(len(data) - 1)
        data.to_csv('expenses.csv', index=False)
        print("\nLatest expense removed successfully.\n")
    else:
        print("\nNo expenses to remove.\n")
    
    return data

while True:
    print('1. Plot expenses')
    print('2. Add expense')
    print('3. Remove latest expense')
    print('4. View expenses')
    print('5. Exit\n')

    while True:
        try:
            choice = int(input('Enter your choice: '))

            if choice in range(1, 6):
                break

            else:
                print('Invalid choice. Please try again.')

        except ValueError:
            print('Invalid choice. Please try again.')  

    if choice == 1:
        plot_expenses(data)

    elif choice == 2:
        data = add_expense(data)  

    elif choice == 3:
        data = remove_expense(data)  

    elif choice == 4:
        print(f"\n{data}\n")   

    else:
        close()
        break

