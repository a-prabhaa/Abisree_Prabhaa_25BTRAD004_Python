class BankAccount:
# Constructor
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = balance  # Encapsulation
    # Deposit money
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid transaction! Deposit amount must be positive.")
        else:
            self.__balance += amount
            print("Amount deposited successfully:", amount)
# Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid transaction! Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print("Amount withdrawn successfully:", amount)
# Check balance
    def check_balance(self):
        print("Available Balance:", self.__balance)
# Display account details
    def display_details(self):
        print("\nAccount Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        self.check_balance()
# Creating an object
account1 = BankAccount("Rahul", 123456, 5000)
# Display account details
account1.display_details(
# Performing banking transactions
print("\n--- Banking Transactions ---")
account1.deposit(2000)
account1.withdraw(1500)
account1.check_balance()

# Testing invalid transactions
print("\n--- Testing Invalid Transactions ---")
account1.deposit(-500)
account1.withdraw(-200)
# Testing insufficient balance
account1.withdraw(10000)
# Final balance
print("\n--- Final Account Details ---")
account1.display_details()
