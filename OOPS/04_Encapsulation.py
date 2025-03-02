'''
Encapsulation (Data Hiding) : It refers to the bundling of data (variables) and methods (functions) that
operate on the data into a single unit (class) and restricting direct access to some details of an object.

Example : 
A bank account has private details (e.g., account balance, PIN) that should not be directly accessible from outside.
'''
class BankAccount:
    def __init__(self,accountHolder,bankBalance):
        self.accountHolder = accountHolder    # Public 
        self.__bankBalance = bankBalance      # Private
    
    # Getter method to access private balance
    def getBalance(self):
        return self.__bankBalance
    
    # Setter method to modify balance securely
    def deposit(self,amount):
        if amount > 0:
            self.__bankBalance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__bankBalance}")
        else:
            print("Invalid deposit amount!")
    
    
account = BankAccount("James Smith",6000)
print(account.accountHolder)
print(account.getBalance())
account.deposit(3000)