class FinancialRecord:
    def __init__(self, record_id, description, amount, record_type, transaction_date):
        self.record_id = record_id
        self.description = description
        self.amount = amount
        self.record_type = record_type  # "Income" or "Expense"
        self.transaction_date = transaction_date

class FinancialModule:
    def __init__(self):
        self.financial_records = []

    def add_income(self, description, amount, transaction_date):
        record_id = len(self.financial_records) + 1
        record = FinancialRecord(record_id, description, amount, "Income", transaction_date)
        self.financial_records.append(record)
        return record

    def add_expense(self, description, amount, transaction_date):
        record_id = len(self.financial_records) + 1
        record = FinancialRecord(record_id, description, amount, "Expense", transaction_date)
        self.financial_records.append(record)
        return record

    def calculate_balance(self):
        income_total = sum(record.amount for record in self.financial_records if record.record_type == "Income")
        expense_total = sum(record.amount for record in self.financial_records if record.record_type == "Expense")
        balance = income_total - expense_total
        return balance

    def view_financial_records(self):
        for record in self.financial_records:
            print(f"Record ID: {record.record_id}")
            print(f"Description: {record.description}")
            print(f"Amount: ${record.amount}")
            print(f"Type: {record.record_type}")
            print(f"Transaction Date: {record.transaction_date}")
            print("\n")

# Example usage
financial_module = FinancialModule()

# Adding income
added_income = financial_module.add_income("Sales Revenue", 5000.0, "2024-02-26")
if added_income:
    print("Income record added successfully!")
else:
    print("Income record addition failed.")

# Adding expense
added_expense = financial_module.add_expense("Office Supplies", 200.0, "2024-02-27")
if added_expense:
    print("Expense record added successfully!")
else:
    print("Expense record addition failed.")

# Calculating balance
current_balance = financial_module.calculate_balance()
print(f"Current Balance: ${current_balance}")

# Viewing financial records
financial_module.view_financial_records()