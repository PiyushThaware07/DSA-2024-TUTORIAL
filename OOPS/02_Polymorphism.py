'''
Polymorphism : In simplest word polymorphism refers to one entity having multiple forms.
               Enables multiple implementations using the same interface or method.
               Methods can have different implementations in different classes.
               
               Different types of accounts (Savings, Current) allow different withdrawal limits or transaction fees, but they all support withdrawals.
               Different accounts have different withdrawal limits
''' 
class BankAccount:
    def __init__(self,accountHolder,bankBalance):
        self.accountHolder = accountHolder
        self.bankBalance = bankBalance
    
    def withdraw(self,amount):
        pass

class SavingAccount(BankAccount):
    def __init__(self, accountHolder, bankBalance):
        super().__init__(accountHolder, bankBalance)
    
    def withdraw(self, amount):
        if amount <= self.bankBalance:
            self.bankBalance -= amount
            return f"Savings withdrawal of {amount}. Remaining Balance: {self.bankBalance}"
        return "Insufficient balance in Savings Account"

class CurrentAccount(BankAccount):
    def __init__(self, accountHolder, bankBalance):
        super().__init__(accountHolder, bankBalance)
    
    def withdraw(self, amount):
        overDraftLimit = 1000  # Extra limit for Current accounts
        if amount <= self.bankBalance + overDraftLimit:
            self.bankBalance -= amount
            return f"Current account withdrawal of {amount}. Remaining Balance: {self.bankBalance}"
        return "Overdraft limit exceeded"

saving = SavingAccount("James Smith",5000)
print(saving.withdraw(1000))

current = CurrentAccount("John Doe",6000)
print(current.withdraw(9000))
