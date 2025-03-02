'''
Abstraction (Hiding Complexity) : Abstraction means hiding implementation details and showing only the 
functionality to the user. It helps in reducing programming complexity and effort.

When you use an ATM, you only see simple options like Withdraw, Deposit, and Check Balance. 
You don’t see the complex banking operations happening in the background.

Abstraction allows users to interact with a system at a high level without worrying about the
underlying complexities.

Sensitive details and implementation logic are hidden from users, reducing risks of accidental 
modification or security vulnerabilities.
'''
from abc import ABC,abstractmethod

class ATM(ABC):
    @abstractmethod
    def withdraw(self,amount):
        pass
    
    @abstractmethod
    def deposit(self,amount):
        pass
    
    @abstractmethod
    def check_balance(self):
        pass

class BankATM(ATM):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ₹{amount} successful. Remaining balance: ₹{self.balance}")
        else:
            print("Insufficient balance or invalid amount!")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ₹{amount} successful. New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount!")

    def check_balance(self):
        print(f"Your current balance is ₹{self.balance}")
        
        
atm = BankATM(6000)
atm.check_balance()
atm.deposit(1000)
atm.withdraw(500)
atm.check_balance()
