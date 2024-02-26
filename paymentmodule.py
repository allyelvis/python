class Payment:
    def __init__(self, payment_id, amount, payment_method, transaction_date):
        self.payment_id = payment_id
        self.amount = amount
        self.payment_method = payment_method
        self.transaction_date = transaction_date

class PaymentModule:
    def __init__(self):
        self.payments = []

    def process_payment(self, amount, payment_method, transaction_date):
        payment_id = len(self.payments) + 1
        payment = Payment(payment_id, amount, payment_method, transaction_date)
        self.payments.append(payment)
        return payment

    def view_payment_history(self):
        for payment in self.payments:
            print(f"Payment ID: {payment.payment_id}")
            print(f"Amount: ${payment.amount}")
            print(f"Payment Method: {payment.payment_method}")
            print(f"Transaction Date: {payment.transaction_date}")
            print("\n")

# Example usage
payment_module = PaymentModule()

# Processing a payment
processed_payment = payment_module.process_payment(100.0, "Credit Card", "2024-02-28")
if processed_payment:
    print("Payment processed successfully!")
else:
    print("Payment processing failed.")

# Viewing payment history
payment_module.view_payment_history()