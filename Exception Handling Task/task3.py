#Banking Management System
class AccountNotFoundError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class OverdraftError(Exception):
    pass

class BankingSystem:
    def __init__(self):
        self.accounts = {}  # acc_id: balance

    def create_account(self, acc_id, initial_balance=0.0):
        if acc_id in self.accounts:
            print(f"Account {acc_id} already exists.")
            return
        if initial_balance < 0:
            raise InvalidAmountError("Initial balance cannot be negative.")
        self.accounts[acc_id] = initial_balance
        print(f"Account {acc_id} created with balance {initial_balance}.")

    def deposit(self, acc_id, amount):
        if acc_id not in self.accounts:
            raise AccountNotFoundError(f"Account {acc_id} not found.")
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive.")
        self.accounts[acc_id] += amount
        print(f"Deposited {amount} to {acc_id}. New balance: {self.accounts[acc_id]}.")

    def withdraw(self, acc_id, amount):
        if acc_id not in self.accounts:
            raise AccountNotFoundError(f"Account {acc_id} not found.")
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if self.accounts[acc_id] < amount:
            raise OverdraftError(f"Insufficient funds. Balance: {self.accounts[acc_id]}, Requested: {amount}.")
        self.accounts[acc_id] -= amount
        print(f"Withdrew {amount} from {acc_id}. New balance: {self.accounts[acc_id]}.")

    def transfer(self, from_acc, to_acc, amount):
        try:
            self.withdraw(from_acc, amount)
            self.deposit(to_acc, amount)
            print(f"Transferred {amount} from {from_acc} to {to_acc}.")
        except (AccountNotFoundError, InvalidAmountError, OverdraftError) as e:
            print(f"Transfer failed: {e}")

    def get_balance(self, acc_id):
        if acc_id not in self.accounts:
            raise AccountNotFoundError(f"Account {acc_id} not found.")
        return self.accounts[acc_id]

    def show_accounts(self):
        for acc, bal in self.accounts.items():
            print(f"Account {acc}: {bal}")

# Example simulation
if __name__ == "__main__":
    bank = BankingSystem()
    
    # Create accounts
    bank.create_account("A001", 1000.0)
    bank.create_account("A002", 500.0)
    
    # Simulate transactions
    bank.deposit("A001", 200.0)
    bank.transfer("A001", "A002", 300.0)
    bank.show_accounts()
    
    # Test errors
    # bank.withdraw("A003", 100)  # Account not found
    # bank.withdraw("A002", 600)  # Overdraft
    # bank.deposit("A001", -50)   # Invalid amount
