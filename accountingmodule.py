class Transaction:
    def __init__(self, transaction_id, description, amount, transaction_type, date):
        self.transaction_id = transaction_id
        self.description = description
        self.amount = amount
        self.transaction_type = transaction_type  # "Income" or "Expense"
        self.date = date

class Account:
    def __init__(self, account_id, name, balance=0.0):
        self.account_id = account_id
        self.name = name
        self.balance = balance

class AccountingModule:
    def __init__(self):
        self.transactions = []
        self.accounts = []

    def create_transaction(self, description, amount, transaction_type, date):
        transaction_id = len(self.transactions) + 1
        transaction = Transaction(transaction_id, description, amount, transaction_type, date)
        self.transactions.append(transaction)
        return transaction

    def create_account(self, name):
        account_id = len(self.accounts) + 1
        account = Account(account_id, name)
        self.accounts.append(account)
        return account

    def process_transaction(self, account, transaction):
        if transaction.transaction_type == "Income":
            account.balance += transaction.amount
        elif transaction.transaction_type == "Expense":
            account.balance -= transaction.amount

    def view_transactions(self):
        for transaction in self.transactions:
            print(f"Transaction ID: {transaction.transaction_id}")
            print(f"Description: {transaction.description}")
            print(f"Amount: ${transaction.amount}")
            print(f"Type: {transaction.transaction_type}")
            print(f"Date: {transaction.date}")
            print("\n")

    def view_accounts(self):
        for account in self.accounts:
            print(f"Account ID: {account.account_id}")
            print(f"Name: {account.name}")
            print(f"Balance: ${account.balance}")
            print("\n")

# Example usage
accounting_module = AccountingModule()

# Creating accounts
cash_account = accounting_module.create_account("Cash")
expenses_account = accounting_module.create_account("Expenses")

# Creating transactions
transaction1 = accounting_module.create_transaction("Sale", 5000.0, "Income", "2024-03-01")
transaction2 = accounting_module.create_transaction("Office Supplies", 200.0, "Expense", "2024-03-02")

# Processing transactions
accounting_module.process_transaction(cash_account, transaction1)
accounting_module.process_transaction(expenses_account, transaction2)

# Viewing transactions and accounts
print("Transactions:")
accounting_module.view_transactions()

print("Accounts:")
accounting_module.view_accounts()