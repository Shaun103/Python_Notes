import tkinter as tk
from tkinter import *
from random import randint

class BankAccount:
    def __init__(self, first_name='xxxxxx', last_name='xxxxxx', type='xxxxxx', number=0, interestRate=0, accBalance=0):
        self.first = first_name
        self.last = last_name
        self.myType = type
        self.interest = interestRate
        self.balance = accBalance

    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def get_balance(self):
        return self.get_balance() * self.accInterest  

class GUI(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title('Bank Account')
        # screen size
        self.geometry("600x400")
        self.title('Bank Account')

        # menu
        menu = Menu(self)
        acct_type_menu = Menu(menu)
        menu.add_cascade(label='Account Type', menu=acct_type_menu)
        acct_type_menu.add_command(label='Standard', command=self.set_type_standard)
        self.config(menu=menu)

        # account
        start_balance = randint(100, 500)
        self.acct = BankAccount(start_balance)

        # first name label
        self.first_label = Label(text='First Name', font=('Times New Roman',10,'normal', 'bold'))
        self.first_label.grid(row=0,column=0)
        # first name entry
        self.first_entry = Entry(font=('Times New Roman',10,'normal', 'bold'))  
        self.first_entry.grid(row=0,column=1)

        # last name label
        self.last_label = Label(text='Last Name', font=('Times New Roman',10,'bold'))
        self.last_label.grid(row=1,column=0)
        # last name entry
        self.last_entry = Entry(font=('Times New Roman',10,'normal', 'bold'))
        self.last_entry.grid(row=1,column=1)

        # account type label
        self.type_label = Label(text='Account Type', font=('Times New Roman',10,'bold'))
        self.type_label.grid(row=2,column=0)
        # account type entry
        self.type_entry = Entry(font=('Times New Roman',10,'normal', 'bold'))
        self.type_entry.grid(row=2,column=1)

        # account number label
        self.number_label = Label(text='Account Number', font=('Times New Roman',10,'bold'))
        self.number_label.grid(row=3,column=0)
        # account number entry
        self.number_entry = Entry(font=('Times New Roman',10,'normal', 'bold'))
        self.number_entry.grid(row=3,column=1)

        # interest rate label
        self.interest_label = Label(text='Interest Rate', font=('Times New Roman',10,'bold'))
        self.interest_label.grid(row=4,column=0)
        # interest rate entry
        self.interest_entry = Entry(font=('Times New Roman',10,'normal', 'bold'))
        self.interest_entry.grid(row=4,column=1)

        # button
        btns_frame = Frame(self)
        btns_frame.grid(row=1,column=1)
    
        # button submit
        Button(text='Submit', width=10, command=self.set_variables).grid(row=0,column=3)

        # button deposit
        Button(text='Deposit', width=10, command=self.deposit).grid(row=1,column=3)

        # button withdraw
        Button(text='Withdraw', width=10, command=self.withdraw).grid(row=2,column=3)
        

        
        Label(self, text='Current Balance:').grid(row=0,column=4)
        
        # default account label
        self.balance_label = Label(self, text='Error: Select account type')
        self.balance_label.grid(row=1,column=4)

        # textbox - withdraw/deposit
        self.text = Entry(self)
        self.text.grid(row=2,column=4)
    
    # bank account type 
    def set_type_standard(self):    
        self.acct_type = 'standard'
        self.balance_label.config(text=self.acct.balance)

    # clears default "Error account type"
    def clear_entry(self):
        self.text.delete(0, END)

    def deposit(self): 
        if self.acct_type == 'standard':
            a = int(self.text.get())
            self.acct.balance += a
            self.balance_label.config(text=self.acct.balance)
            print('..amount deposited')
        else:
            self.balance_label.config(text='Error: Select account type')
        self.clear_entry()

    def withdraw(self):
        a = int(self.text.get())
        if self.acct_type == 'standard': 
            if self.acct.balance < a:
                print('..insufficient funds')
            else:  
                self.acct.balance -= a
                self.balance_label.config(text=self.acct.balance)
                print('..amount withdrawn')
        else:
            self.balance_label.config(text='Error: Select account type')
        self.clear_entry()

    # sets object class 
    def set_variables(self):
        first = str(self.first_entry.get())
        self.acct.first = first
        last = str(self.last_entry.get())
        self.acct.last = last
        type = str(self.type_entry.get())
        self.acct.type = type
        number = int(self.number_entry.get())
        self.acct.number = number
        interest = float(self.interest_entry.get())
        self.acct.interestRate = interest

        # error/bug checking
        print("First name: ", first)
        print("Last name: ", last)
        print("Account type: ", type)
        print("Account number: ", number)
        print("Account interest rate: ", interest) 

if __name__ == '__main__':
    GUI().mainloop()