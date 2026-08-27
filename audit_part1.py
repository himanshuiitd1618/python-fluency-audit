# Task 1: The Base Class
class BankAccount:
    def __init__(self):
        # When we create an account, it starts with 0 balance
        self.balance = 0

    def deposit(self, amount: float) -> None:
        # Add money to the balance
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount: float) -> None:
        # Check if they have enough money
        if amount > self.balance:
            # Raise an error if they don't
            raise ValueError(f"Insufficient funds! You have {self.balance}, tried to withdraw {amount}.")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

# Task 2: The Child Class (Inheritance)
class SavingsAccount(BankAccount):
    # It inherits everything from BankAccount, but changes the withdraw rule
    def withdraw(self, amount: float) -> None:
        if self.balance - amount < 100:
            raise ValueError("Cannot withdraw: Savings accounts must maintain a minimum $100 balance.")
        # If the rule passes, we run the normal math by calling the parent's logic directly
        self.balance -= amount
        print(f"Withdrew {amount} from Savings. New balance: {self.balance}")

# --- Testing the code ---
print("--- Testing BankAccount ---")
my_account = BankAccount()
my_account.deposit(50)
my_account.withdraw(20)

print("\n--- Testing SavingsAccount ---")
my_savings = SavingsAccount()
my_savings.deposit(150) # Must deposit at least 100 to keep it open
try:
    my_savings.withdraw(60) # This will fail because 150 - 60 = 90, which is below 100
except ValueError as e:
    print(f"Error caught: {e}")
# Task 3: List Comprehensions
print("\n--- Testing List Comprehension ---")
users = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 17},
    {'name': 'Charlie', 'age': 30},
    {'name': 'David', 'age': 15}
]

# The long way (don't do this):
# adult_names = []
# for user in users:
#     if user['age'] >= 18:
#         adult_names.append(user['name'])

# The Pythonic way (List Comprehension):
adult_names = [user['name'] for user in users if user['age'] >= 18]

print(f"Adults: {adult_names}")
