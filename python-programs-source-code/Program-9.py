class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Encapsulated attribute
        self.__balance = balance  # Encapsulated attribute

    def deposit(self, amount):
        """Method to deposit money into the account."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """Method to withdraw money from the account."""
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        """Method to get the current balance."""
        return self.__balance

    def get_account_number(self):
        """Method to get the account number."""
        return self.__account_number

# Creating a BankAccount object
account = BankAccount("123456789", 1000)

# Accessing encapsulated attributes directly (shouldn't be done)
# print(account.__account_number)  # This will raise an AttributeError

# Accessing encapsulated attributes using getter methods
print("Account Number:", account.get_account_number())
print("Balance:", account.get_balance())

# Depositing and withdrawing money
account.deposit(500)
account.withdraw(200)
