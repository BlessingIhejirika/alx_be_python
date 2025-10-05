class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize account with an optional starting balance."""
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        """Add funds to the account balance."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw funds if available. Returns True if successful."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Prints the current balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")

    def get_balance(self):
        """Getter for balance (not directly exposed to users)."""
        return self.__account_balance
