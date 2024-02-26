class PurchaseOrder:
    def __init__(self, order_id, vendor_id, products, total_amount, order_date, status):
        self.order_id = order_id
        self.vendor_id = vendor_id
        self.products = products
        self.total_amount = total_amount
        self.order_date = order_date
        self.status = status  # "Pending", "Approved", "Rejected"

class PurchaseModule:
    def __init__(self, inventory):
        self.purchase_orders = []
        self.inventory = inventory

    def create_purchase_order(self, vendor_id, products):
        total_amount = sum(product['price'] * product['quantity'] for product in products)
        order_id = len(self.purchase_orders) + 1
        order = PurchaseOrder(order_id, vendor_id, products, total_amount, "2024-02-29", "Pending")
        self.purchase_orders.append(order)
        return order

    def approve_purchase_order(self, order_id):
        order = self.get_order_by_id(order_id)
        if order and order.status == "Pending":
            order.status = "Approved"
            # Update inventory after approving purchase order
            for product in order.products:
                product_id = product['product_id']
                quantity = product['quantity']
                self.inventory.update_product(product_id, quantity)
            return True
        else:
            return False

    def reject_purchase_order(self, order_id):
        order = self.get_order_by_id(order_id)
        if order and order.status == "Pending":
            order.status = "Rejected"
            return True
        else:
            return False

    def get_order_by_id(self, order_id):
        for order in self.purchase_orders:
            if order.order_id == order_id:
                return order
        return None

    def view_purchase_orders(self):
        for order in self.purchase_orders:
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
purchase_module = PurchaseModule(inventory_system)

# Creating a purchase order
products_to_order = [
    {'product_id': 1, 'quantity': 5},
    {'product_id': 2, 'quantity': 3},
]
created_order = purchase_module.create_purchase_order(vendor_id=1, products=products_to_order)
if created_order:
    print("Purchase order created successfully!")
else:
    print("Purchase order creation failed. Invalid vendor ID or product ID.")

# Approving a purchase order
approved_order = purchase_module.approve_purchase_order(1)
if approved_order:
    print("Purchase order approved successfully!")
else:
    print("Purchase order approval failed. Invalid order ID or already approved/rejected.")

# Rejecting a purchase order
rejected_order = purchase_module.reject_purchase_order(1)
if rejected_order:
    print("Purchase order rejected successfully!")
else:
    print("Purchase order rejection failed. Invalid order ID or already approved/rejected.")

# Viewing purchase orders
purchase_module.view_purchase_orders()