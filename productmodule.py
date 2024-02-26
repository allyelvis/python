class Product:
    def __init__(self, product_id, name, description, price, quantity):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class ProductModule:
    def __init__(self):
        self.products = []

    def add_product(self, name, description, price, quantity):
        product_id = len(self.products) + 1
        product = Product(product_id, name, description, price, quantity)
        self.products.append(product)
        return product

    def update_product(self, product_id, name=None, description=None, price=None, quantity=None):
        product = self.get_product_by_id(product_id)
        if product:
            if name is not None:
                product.name = name
            if description is not None:
                product.description = description
            if price is not None:
                product.price = price
            if quantity is not None:
                product.quantity = quantity
            return True
        else:
            return False

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def view_product_list(self):
        for product in self.products:
            print(f"Product ID: {product.product_id}")
            print(f"Name: {product.name}")
            print(f"Description: {product.description}")
            print(f"Price: ${product.price}")
            print(f"Quantity in Stock: {product.quantity}")
            print("\n")

# Example usage
product_module = ProductModule()

# Adding a product
added_product = product_module.add_product("Laptop", "High-performance laptop", 1200.0, 50)
if added_product:
    print("Product added successfully!")
else:
    print("Product addition failed.")

# Updating a product
updated_product = product_module.update_product(1, price=1300.0, quantity=45)
if updated_product:
    print("Product updated successfully!")
else:
    print("Product update failed. Invalid product ID.")

# Viewing the product list
product_module.view_product_list()