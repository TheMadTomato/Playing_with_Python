"""
Problem 2: Bank Account
Write a Python class BankAccount with attributes like account_number, balance, date_of_opening
and customer_name, and methods like deposit, withdraw, and check_balance.
"""
import time

class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful.")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdraw successful.")


    def logs(self):
        print("---------------------------------------------------")
        print("Account Number: ", self.account_number)
        print("Customer Name: ", self.customer_name)
        print("Date of Opening: ", self.date_of_opening)
        print("Balance: ", self.balance)
        print("Date: ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("---------------------------------------------------")

    def check_balance(self):
        print("Balance: ", self.balance)


MyBankAccount = BankAccount(12220605, 10000, "2021-09-01", "Paul")

MyBankAccount.check_balance()
MyBankAccount.deposit(5000)
MyBankAccount.check_balance()
MyBankAccount.withdraw(20000)
MyBankAccount.check_balance()
MyBankAccount.withdraw(5000)
MyBankAccount.check_balance()
MyBankAccount.logs()

