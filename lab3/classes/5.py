class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.owner} : Deposited {amount}. New balance: {self.balance}")
        else:
            print(f"{self.owner} : Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} : Withdrew {amount}. New balance: {self.balance}")
        else:
            print(f"{self.owner} : Insufficient funds or invalid amount.")
            

client1 = Account("Maks", 456000)

client1.withdraw(456000)

account = Account("Alex", 100.0)
account.deposit(50)
account.withdraw(30)
account.withdraw(150)