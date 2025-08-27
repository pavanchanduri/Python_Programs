class Dog:
    ## Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

dog1 = Dog("Buddy", 5)
dog1.display()

class Bank:
    ## Constructor
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print(f"Account Holder: {self.name}, Balance: {self.balance}")

    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}, New Balance: {self.balance}")

bank1 = Bank("Alice", 1000)
bank1.display()
bank1.deposit(500)
bank1.withdraw(200)
bank1.display()