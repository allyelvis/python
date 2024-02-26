class Product:
    def __init__(self, product_id, name, description, price, quantity):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def update_product(self, product_id, new_quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.quantity = new_quantity
                return True
        return False

    def view_stock(self):
        for product in self.products:
            print(f"{product.name}: {product.quantity} units")

# Example usage
inventory_system = Inventory()

# Adding products
product1 = Product(1, "Laptop", "High-performance laptop", 1200.0, 50)
product2 = Product(2, "Printer", "Color laser printer", 300.0, 20)

inventory_system.add_product(product1)
inventory_system.add_product(product2)

# Updating stock
inventory_system.update_product(1, 45)

# Viewing stock
inventory_system.view_stock()