class ReportsModule:
    def __init__(self, inventory, sales_module, financial_module, purchase_module):
        self.inventory = inventory
        self.sales_module = sales_module
        self.financial_module = financial_module
        self.purchase_module = purchase_module

    def generate_inventory_report(self):
        print("Inventory Report:")
        for product in self.inventory.products:
            print(f"Product ID: {product.product_id}")
            print(f"Name: {product.name}")
            print(f"Quantity in Stock: {product.quantity}")
            print("\n")

    def generate_sales_report(self):
        print("Sales Report:")
        for sale in self.sales_module.sales:
            print(f"Sale ID: {sale.sale_id}")
            print(f"Date: {sale.sale_date}")
            print(f"Total Amount: ${sale.total_amount}")
            print("Products:")
            for product, quantity in sale.products:
                print(f"  - {product}: {quantity} units")
            print("\n")

    def generate_financial_report(self):
        print("Financial Report:")
        for record in self.financial_module.financial_records:
            print(f"Record ID: {record.record_id}")
            print(f"Description: {record.description}")
            print(f"Amount: ${record.amount}")
            print(f"Type: {record.record_type}")
            print(f"Transaction Date: {record.transaction_date}")
            print("\n")

    def generate_purchase_report(self):
        print("Purchase Report:")
        for order in self.purchase_module.purchase_orders:
            print(f"Order ID: {order.order_id}")
            print(f"Vendor ID: {order.vendor_id}")
            print("Products:")
            for product in order.products:
                print(f"  - Product ID: {product['product_id']}, Quantity: {product['quantity']}")
            print(f"Total Amount: ${order.total_amount}")
            print(f"Order Date: {order.order_date}")
            print(f"Status: {order.status}")
            print("\n")

# Example usage
reports_module = ReportsModule(inventory_system, sales_module, financial_module, purchase_module)

# Generating reports
reports_module.generate_inventory_report()
reports_module.generate_sales_report()
reports_module.generate_financial_report()
reports_module.generate_purchase_report()