import tkinter
from tkinter import *
from random import randint

class Account:
    def __init__(self, init_balance=0):
        self.balance = init_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def get_balance(self, init_balance, rate):
        return self.get_balance() * self._rate

class InterestAccount(Account):
    def __init__(self, init_balance=0, rate=0.1):
        super().__init__(init_balance)
        self._rate = rate
    def interest(self):
        return self.balance * self._rate

class GUI(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Bank Account')

        #Menu#
        menu = Menu(self)
        acct_type_menu = Menu(menu)
        menu.add_cascade(label='Account Type', menu=acct_type_menu)
        acct_type_menu.add_command(label='Standard', command=self.set_type_standard)
        acct_type_menu.add_command(label='Interest', command=self.set_type_interest)
        self.config(menu=menu)

        #Account#
        start_balance = randint(100, 500)
        self.acct = Account(start_balance)
        self.my_interest = InterestAccount(start_balance)
        self.interest = self.my_interest.balance + self.my_interest.interest()

        #Labels#
        Label(self, text='Current Balance:').pack()
        self.balance_label = Label(self, text='Error: Select account type')
        self.balance_label.pack()

        #Button#
        btns_frame = Frame(self)
        btns_frame.pack(side=TOP, fill=X)

        Button(btns_frame, text='Deposit', width=13, command=self.deposit).pack(side=LEFT)
        Button(btns_frame, text='Withdraw', width=13, command=self.withdraw).pack(side=RIGHT)

        #Textbox#
        self.text = Entry(self)
        self.text.pack()

    def set_type_standard(self):
        self.acct_type = 'standard'
        self.balance_label.config(text=self.acct.balance)

    def set_type_interest(self):
        self.acct_type = 'interest'
        self.balance_label.config(text=self.interest)

    def clear_entry(self):
        self.text.delete(0, END)

    def deposit(self): 
        if self.acct_type == 'interest':
            a = int(self.text.get())
            self.interest += a
            self.balance_label.config(text=self.interest)
        elif self.acct_type == 'standard':
            a = int(self.text.get())
            self.acct.balance += a
            self.balance_label.config(text=self.acct.balance)
        else:
            self.balance_label.config(text='Error: Select account type')
        self.clear_entry()

    def withdraw(self):
        if self.acct_type == 'interest':
            a = int(self.text.get())
            self.interest -= a
            self.balance_label.config(text=self.interest)
        elif self.acct_type == 'standard':
            a = int(self.text.get())
            self.acct.balance -= a
            self.balance_label.config(text=self.acct.balance)
        else:
            self.balance_label.config(text='Error: Select account type')
        self.clear_entry()

if __name__ == '__main__':
    GUI().mainloop()