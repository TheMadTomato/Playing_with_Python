class ATM:
    def __init__(self, pin, bdl_balance, fd_balance, lbp_balance):
        # define attributes 'pin' for the password and the rest for the 3 different type of accounts
        self.pin = pin
        self.bdl_balance = bdl_balance
        self.fd_balance = fd_balance
        self.lbp_balance = lbp_balance

    def check_pin(self, pin):
        if pin == self.pin:
            return True
        return False

    def withdraw_151(self, amount):
        if amount <= self.bdl_balance / 8000:
            self.bdl_balance -= amount * 8000
            return amount
        else:
            return "You don't have enough balance"
    def withdraw_fd(self, amount):
        if amount <= self.fd_balance:
            self.fd_balance -= amount
            return amount
        else:
            return "You don't have enough balance"
    def withdraw_lbp(self, amount):
        if amount <= self.lbp_balance:
            self.lbp_balance -= amount
            return amount
        else:
            return "You don't have enough balance"

    def check_balance(self):
        print("\nBDL;\t\tFD;\t\tLBP")
        return self.bdl_balance, self.fd_balance, self.lbp_balance

    def start(self):
        tries = 0
        while tries < 3:
            pin = input("Enter your pin: ")
            if self.check_pin(pin):
                print("Welcome")
                self.choose_option()
                break
            else:
                tries += 1
                print("Incorrect pin")
    def choose_option(self):
        while True:
            print("\nChoose an option:")
            print("1. Withdraw Circular 151 BDL")
            print("2. Withdraw Fresh Dollar")
            print("3. Withdraw LBP")
            print("4. Check Balance")
            print("5. Exit")
            print()
            option = input("Enter your option: ")
            if option == "1":
                amount = int(input("Enter the amount: "))
                print(self.withdraw_151(amount))
            elif option == "2":
                amount = int(input("Enter the amount: "))
                print(self.withdraw_fd(amount))
            elif option == "3":
                amount = int(input("Enter the amount: "))
                print(self.withdraw_lbp(amount))
            elif option == "4":
                print(self.check_balance())
            elif option == "5":
                break
            else:
                print("Invalid option")

# test
atm = ATM("1234", 100000, 100000, 100000)
atm.start()

