class Sale:
    def __init__(self, sale_id, products, total_amount, sale_date):
        self.sale_id = sale_id
        self.products = products
        self.total_amount = total_amount
        self.sale_date = sale_date

class SalesModule:
    def __init__(self, inventory):
        self.sales = []
        self.inventory = inventory

    def create_sale(self, product_id, quantity):
        product = self.get_product_by_id(product_id)
        if product and product.quantity >= quantity:
            sale_id = len(self.sales) + 1
            total_amount = product.price * quantity
            sale = Sale(sale_id, [(product.name, quantity)], total_amount, "2024-02-26")
            
            # Update inventory after the sale
            self.inventory.update_product(product_id, product.quantity - quantity)

            self.sales.append(sale)
            return sale
        else:
            return None

    def get_product_by_id(self, product_id):
        for product in self.inventory.products:
            if product.product_id == product_id:
                return product
        return None

    def view_sales_history(self):
        for sale in self.sales:
            print(f"Sale ID: {sale.sale_id}, Date: {sale.sale_date}, Total Amount: ${sale.total_amount}")
            for product, quantity in sale.products:
                print(f"  - {product}: {quantity} units")

# Example usage
sales_module = SalesModule(inventory_system)

# Creating a sale
created_sale = sales_module.create_sale(1, 3)

if created_sale:
    print("Sale successful!")
else:
    print("Sale failed. Insufficient stock or invalid product ID.")

# Viewing sales history
sales_module.view_sales_history()