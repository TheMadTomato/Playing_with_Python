"""
Write a Python class BankAccount with attributes like account_number, balance,
date_of_opening and customer_name, and methods like deposit, withdraw, and
check_balance.
"""
class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        print(f"You deposited {amount}. Your new balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("You don't have enough money to withdraw")
        else:
            self.balance -= amount
            print(f"You withdrawn {amount}. Your new balance is {self.balance}")

    def check_balance(self):
        print(f"Your balance is {self.balance}")

# test
account1 = BankAccount(123456789, 1000, "01/01/2021", "Paul Estehan")

print("Welcome to your bank account")
account1.check_balance()
account1.deposit(500)
account1.withdraw(200)
account1.check_balance()