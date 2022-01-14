import tkinter as tk

class BankAccount:
    def __init__(self, first_name='xxxxxx', last_name='xxxxxx', type='xxxxxx', number=0, interestRate=0, balance=0):
        self.accFirstName = first_name
        self.accLastName = last_name
        self.accType = type
        self.accNumber = number
        self.accInterestRate = interestRate
        self.accBalance = balance

# creating instances of the class
a = BankAccount() 

def set_variables():
    first = a.accFirstName.get()
    last = a.accLastName.get()
    type = a.accType.get()
    number = a.accNumber.get()
    interestRate = a.accInterestRate.get()

    print("First name: ", first)
    print("Last name: ", last)
    print("Account type: ", type)
    print("Account number: ", number)
    print("Account interest rate: ", interestRate)

# def withdraw(self, withdrawAmount):
#     if self.accBalance >= withdrawAmount:
#         self.accBalance -= withdrawAmount
#     else:
#         raise AttributeError(f"...insufficient balance") 
            
def deposit(self, amount):
    self.balance += amount
    print("Account balance: ", a.accBalance.get())

def withdraw():
    pass

def main() -> None:
    mainWindow = tk.Tk()
    mainWindow.geometry("600x400")

    # class variables that tkinter with manipulate 
    a.accFirstName=tk.StringVar()
    a.accLastName=tk.StringVar()
    a.accType=tk.StringVar()
    a.accNumber=tk.IntVar()
    a.accInterestRate=tk.DoubleVar()
    a.accBalance=tk.DoubleVar()

    # assigning what is in labels and fields
    first_label = tk.Label(mainWindow, text='First name', font=('Times New Roman',10, 'bold'))
    first_entry = tk.Entry(mainWindow, textvariable = a.accFirstName, font=('Times New Roman',10,'normal'))

    last_label = tk.Label(mainWindow, text='Last name', font=('Times New Roman',10, 'bold'))
    last_entry = tk.Entry(mainWindow, textvariable = a.accLastName, font=('Times New Roman',10,'normal'))

    type_label = tk.Label(mainWindow, text='Account Type', font=('Times New Roman',10, 'bold'))
    type_entry = tk.Entry(mainWindow, textvariable = a.accType, font=('Times New Roman',10,'normal'))

    number_label = tk.Label(mainWindow, text='Account number', font=('Times New Roman',10, 'bold'))
    number_entry = tk.Entry(mainWindow, textvariable = a.accNumber, font=('Times New Roman',10,'normal'))

    interest_label = tk.Label(mainWindow, text='Interest rate', font=('Times New Roman',10, 'bold'))
    interest_entry = tk.Entry(mainWindow, textvariable = a.accInterestRate, font=('Times New Roman',10,'normal'))

    deposit_label = tk.Label(mainWindow, text='Balance', font=('Times New Roman',10, 'bold'))
    deposit_entry = tk.Entry(mainWindow, textvariable = a.accBalance, font=('Times New Roman',10,'normal'))

    withdraw_label = tk.Label(mainWindow, text='Balance', font=('Times New Roman',10, 'bold'))
    withdraw_entry = tk.Entry(mainWindow, textvariable = a.accBalance, font=('Times New Roman',10,'normal'))

    sub_btn=tk.Button(mainWindow,text='Show', command=set_variables)

    deposit_btn=tk.Button(mainWindow,text='Deposit', command=deposit) 
    withdraw_btn=tk.Button(mainWindow,text='Withdraw', command=withdraw) 

    # displaying fields labels
    first_label.grid(row=0,column=0)
    first_entry.grid(row=0,column=1)

    last_label.grid(row=1,column=0)
    last_entry.grid(row=1,column=1)

    type_label.grid(row=2,column=0)
    type_entry.grid(row=2,column=1)

    number_label.grid(row=3,column=0)
    number_entry.grid(row=3,column=1)

    interest_label.grid(row=4,column=0)
    interest_entry.grid(row=4,column=1)

    deposit_label.grid(row=5,column=0)
    deposit_entry.grid(row=5,column=1)
    
    deposit_label.grid(row=6,column=0)
    deposit_entry.grid(row=6,column=1)
    
    sub_btn.grid(row=7,column=0)        # submit button

    deposit_btn.grid(row=7,column=1)    # deposit button
    withdraw_btn.grid(row=7,column=2)   # withdraw button

    tk.mainloop()

if __name__ == "__main__":
    main()