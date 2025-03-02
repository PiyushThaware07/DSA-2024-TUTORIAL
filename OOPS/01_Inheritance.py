'''
Inheritance : In simplest word inheritance means creating new class based on the exiting class
              Inherit the properties and behaviors of parent class into the child class.
              It allows overriding of methods in child class.
              
              Example : A Savings Account and a Current Account are types of Bank Accounts, but each has different behaviors
              Savings and Current accounts inherit common bank features
'''
class BankAccount:
    def __init__(self,accountHolder,bankBalance):
        self.accountHolder = accountHolder
        self.bankBalance = bankBalance
    
    def deposit(self,amount):
        self.bankBalance += amount
        return f"{amount} deposited. New balance: {self.bankBalance}"

class SavingAccount(BankAccount):
    def __init__(self, accountHolder, bankBalance,interestRate):
        super().__init__(accountHolder, bankBalance)
        self.interestRate = interestRate
    
    def addInterest(self):
        interest = self.bankBalance * self.interestRate / 100
        self.bankBalance += interest
        return f"Interest added: {interest}. New Balance: {self.bankBalance}"

class CurrentAccount(BankAccount):
    def __init__(self, accountHolder, bankBalance, overdraftLimit):
        super().__init__(accountHolder, bankBalance)
        self.overdraftLimit = overdraftLimit
    
    def withdraw(self, amount):
        if amount > self.bankBalance + self.overdraftLimit:
            return "Insufficient Funds"
        else:
            self.bankBalance -= amount
            return f"{amount} withdrawn. New balance: {self.bankBalance}"
            

    
saving = SavingAccount("James Smith",10000,5)
print(saving.deposit(100))
print(saving.addInterest())


current = CurrentAccount("John Doe",5000,1000)
print(current.withdraw(7000))