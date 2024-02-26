class Order:
    def __init__(self, order_id, products, total_amount, order_date):
        self.order_id = order_id
        self.products = products
        self.total_amount = total_amount
        self.order_date = order_date

class OrderModule:
    def __init__(self, inventory):
        self.orders = []
        self.inventory = inventory

    def create_order(self, product_id, quantity):
        product = self.get_product_by_id(product_id)
        if product and product.quantity >= quantity:
            order_id = len(self.orders) + 1
            total_amount = product.price * quantity
            order = Order(order_id, [(product.name, quantity)], total_amount, "2024-02-26")
            
            # Update inventory after the order
            self.inventory.update_product(product_id, product.quantity - quantity)

            self.orders.append(order)
            return order
        else:
            return None

    def get_product_by_id(self, product_id):
        for product in self.inventory.products:
            if product.product_id == product_id:
                return product
        return None

    def view_order_history(self):
        for order in self.orders:
            print(f"Order ID: {order.order_id}, Date: {order.order_date}, Total Amount: ${order.total_amount}")
            for product, quantity in order.products:
                print(f"  - {product}: {quantity} units")

# Example usage
order_module = OrderModule(inventory_system)

# Creating an order
created_order = order_module.create_order(2, 2)

if created_order:
    print("Order successful!")
else:
    print("Order failed. Insufficient stock or invalid product ID.")

# Viewing order history
order_module.view_order_history()