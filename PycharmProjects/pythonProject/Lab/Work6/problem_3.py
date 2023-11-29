"""
Problem 3: ATM
Due to the economic crisis in Lebanon and the limit in money withdraw. Your Bank [ Bank of
AUST] asked you to develop a python program to let the clients do the following.
1- Client should enter his/her Pin
1. Only let the user enter numbers no character.
2. If authentication failed, then keep asking to enter the password. If client tried 3 then
system block his/her account.
the Authentication client will select one of the below options

1. Withdraw Circular 151 BDL ( Banque Du Liban ) 1$=8,000 LBP
2. Withdraw Fresh Dollar $ from FD account
3. Withdraw LBP from LBP account
4. Check Balance.

N.B : - Make the 3 different attribtes for the client ( 151 BDL, LBP account, and FD account)
      - The '151 BDL' is an account that store money in LBP but the client can withdraw it in
        dollars with the rate of 151 BDL.
      - Make sure that the client can't withdraw more than his/her balance. and if he/she tried
        to withdraw more than the balance then print "You don't have enough balance".
"""

class ATM:
    def __init__(self, pin, bdl151_balance, fd_balance, lbp_balance):
        # define attributes 'pin' for the password and the rest for the 3 different type of accounts
        self.pin = pin
        self.bdl151_balance = bdl151_balance
        self.fd_balance = fd_balance
        self.lbp_balance = lbp_balance

    def check_pin(self, pin):
        # check if the pin is correct. the 'allow only 3 tries' feature is implemented in start() method
        if pin == self.pin:
            return True
        return False

    def withdraw_151(self, amount):
        # check if the amount is less than the balance stored in the 151 BDL account.
        # if so, withdraw the amount and return it. otherwise, return a message
        # the amount is compared to the balance divided by 8000 because 1$ = 8000 LBP
        # and the withdrawn is in dollars but the amount is in LBP
        if amount <= self.bdl151_balance / 8000:
            self.bdl151_balance -= amount * 8000
            return amount
        else:
            return "You don't have enough balance"

    def withdraw_fd(self, amount):
        # check if the amount is less than the balance stored in the FD account.
        # if so, withdraw the amount and return it. otherwise, return a message
        if amount <= self.fd_balance:
            self.fd_balance -= amount
            return amount
        else:
            return "You don't have enough balance"

    def withdraw_lbp(self, amount):
        # check if the amount is less than the balance stored in the LBP account.
        # if so, withdraw the amount and return it. otherwise, return a message
        if amount <= self.lbp_balance:
            self.lbp_balance -= amount
            return amount
        else:
            return "You don't have enough balance"

    # Check the balance of each account
    def check_bdl151_balance(self):
        return self.bdl151_balance

    def check_fd_balance(self):
        return self.fd_balance

    def check_lbp_balance(self):
        return self.lbp_balance

    # Deposit in each account
    def deposit_bdl151(self, amount):
        self.bdl151_balance += amount

    def deposit_fd(self, amount):
        self.fd_balance += amount

    def deposit_lbp(self, amount):
        self.lbp_balance += amount

    def start(self):
        # allow only 3 tries to enter the pin. if the pin is correct, then the user can use the ATM
        # otherwise, the account is blocked.
        for i in range(3):
            pin = input("Enter your pin: ")
            if self.check_pin(pin):
                # Formatted menu to make the output look clean and organized
                print("Welcome to Bank of AUST".center(61, "-"))
                while True:
                    print("-"*61)
                    print("1. Withdraw Circular 151 BDL ( Banque Du Liban ) 1$=8,000 LBP")
                    print("2. Withdraw Fresh Dollar $ from FD account")
                    print("3. Withdraw LBP from LBP account")
                    print("4. Check Balance")
                    print("5. Deposit in BDL 151")
                    print("6. Deposit in FD")
                    print("7. Deposit in LBP")
                    print("8. Exit")
                    print("-" * 61)

                    # the user can choose one of the options from the menu
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        amount = int(input("Enter the amount: "))
                        print("You have successfully withdrawn", self.withdraw_151(amount), "$")
                    elif choice == 2:
                        amount = int(input("Enter the amount: "))
                        print("You have successfully withdrawn", self.withdraw_fd(amount), "$")
                    elif choice == 3:
                        amount = int(input("Enter the amount: "))
                        print("You have successfully withdrawn", self.withdraw_lbp(amount), "LBP")
                    elif choice == 4:
                        print("Your balance is", self.check_bdl151_balance(), "LBP")
                        print("Your FD balance is", self.check_fd_balance(), "$")
                        print("Your LBP balance is", self.check_lbp_balance(), "LBP")
                    elif choice == 5:
                        amount = int(input("Enter the amount (in LBP): "))
                        self.deposit_bdl151(amount)
                        print("You have successfully deposited", amount, "LBP")
                    elif choice == 6:
                        amount = int(input("Enter the amount: "))
                        self.deposit_fd(amount)
                        print("You have successfully deposited", amount, "$")
                    elif choice == 7:
                        amount = int(input("Enter the amount: "))
                        self.deposit_lbp(amount)
                        print("You have successfully deposited", amount, "LBP")
                    elif choice == 8:
                        print("Thank you for using our service")
                        exit()
                    else:
                        print("Wrong choice, try again")
            else:
                print("Wrong pin, try again")
        print("Your account is blocked")
        exit()


# create an object from the class ATM and start the program.
# values are just for testing. you can change them.
client = ATM("1234", 100000, 1000, 1000000)
client.start()
