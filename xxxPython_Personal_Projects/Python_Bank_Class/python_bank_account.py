class BankAccount:
    def __init__(self, first_name='xxxxxx', last_name='xxxxxx', type='xxxxxx', number=0, balance=0, interestRate=0):
        self.accFirstName = first_name
        self.accLastName = last_name
        self.accType = type
        self.accNumber = number
        self.accBalance = balance
        self.accInterestRate = interestRate
    
    def withdraw(self, withdrawAmount):
        if self.accBalance >= withdrawAmount:
            self.accBalance -= withdrawAmount
        else:
            raise AttributeError(f"...insufficient balance") 
            
    def deposit(self, depositAmount):
        self.accBalance += depositAmount
    
    def __setattr__(self, name, value):
        # print(f">>> You set {name} = {value}") # checking to see if the method works
        self.__dict__[name] = value

    def __str__(self): # prints account information
        return f"{self.accFirstName} {self.accLastName} {self.accType} account {self.accNumber} {self.accBalance} {self.accInterestRate}"

    def __getattr__(self, name):
        # print(f">>> Get the '{name}' attribute") # checking to see if the method works
        if name == 'full_name':
            return f"{self.accFirstName} {self.accLastName}"
        else:
            raise AttributeError(f"No attribute named {name}") 
    
    # will help the sort function
    def __lt__(self, rhs):
        # print(f">>> Comparing {self.accLastName} with {rhs.accLastName}") # checking to see if the method works
        if self.accLastName != rhs.accLastName:
            return (self.accLastName < rhs.accLastName)
        else:
            return (self.accFirstName < rhs.accFirstName)

def main():

    a = BankAccount('Arthur', 'Arya', 'Checking', 1, 55000.00, 3.6)
    b = BankAccount('Peter', 'Parker', 'Savings', 222, 200.00, 0.2)
    c = BankAccount('Craig', 'Cleesonmonte', 'Checking', 444, 3000.00, 3.6)
    d = BankAccount('Sansa', 'Stark', 'Savings', 333, 900.00, 0.9)
    e = BankAccount('Bam', 'Bennsonton', 'Checking', 111, 4000.00, 0.3)
    
    print('\n')

    acc = [a, b, c, d, e]
    
    acc.sort()

    for a in acc:
        print(a)
        
    print('\n')

    print(b)

    b.withdraw(100)
    b.deposit(1000)

    print(b)

    print('\n')
    
    c.accBalance = 100
    
    print(c)
    


if __name__ == '__main__':
    main()