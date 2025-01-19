class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance}")
