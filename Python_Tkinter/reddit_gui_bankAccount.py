import tkinter as tk
from tkinter.messagebox import showinfo

class InsufficentFundError(Exception):
    pass

class BankAccount:
    """bank account class"""
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            raise InsufficentFundError

    def deposit(self, amount):
        self.balance += amount

class ATM(tk.Tk):
    def __init__(self,account=None):
        tk.Tk.__init__(self)

        self.title('ATM')

        if account is None:
            self.account = BankAccount()
        else:
            self.account = account

        self.make_widgets()
        self.updateBalance()

    def withdraw(self):
        """withdraw funds from BankAccount and update GUI"""
        try:
            amount = float(self.iEntry.get())
            self.account.withdraw(amount)
            showinfo(title='transaction',message='successful withdrawal')
        except ValueError:
            showinfo(title='Transaction',message='Amount entered is not a number')
        except InsufficentFundError:
            showinfo(title='transaction',message='error. unable to withdraw funds.')

        self.iEntry.delete(0, tk.END)
        self.updateBalance()

    def deposit(self):
        """add funds to BankAccount and update GUI"""
        try:
            amount = float(self.iEntry.get())
            self.account.deposit(amount)
            showinfo(title='transaction',message='successful deposit')
        except ValueError:
            showinfo(title="Transaction",message='Amount entered is not a number')

        self.iEntry.delete(0, tk.END)
        self.updateBalance()

    def updateBalance(self):
        """Update account balance label in GUI"""
        self.updatedbalance.config(text=str(self.account.balance))

    def make_widgets(self):
        """Create widgets"""
        lbl = tk.Label(self,text='Balance:')
        lbl.grid(row = 0, column = 0)

        self.updatedbalance = tk.Label(self,text='')
        self.updatedbalance.grid(row = 0, column= 1)

        lbl = tk.Label(self,text="Amount:")
        lbl.grid(row = 1,column = 0)

        self.iEntry = tk.Entry(self,width=40)
        self.iEntry.grid(row=1,column=1)

        a = tk.Button(self,text='Withdraw',command=self.withdraw)
        a.grid(row=2,column=0)
        
        b = tk.Button(self,text='Deposit',command=self.deposit)
        b.grid(row=2,column=1)

root = ATM()
root.mainloop()