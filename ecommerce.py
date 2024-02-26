class Product:
    def __init__(self, product_id, name, description, price, quantity):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class User:
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password

class Order:
    def __init__(self, order_id, user, products, total_amount, order_date, status):
        self.order_id = order_id
        self.user = user
        self.products = products
        self.total_amount = total_amount
        self.order_date = order_date
        self.status = status  # "Pending", "Shipped", "Delivered"

class ECommerceModule:
    def __init__(self):
        self.products = []
        self.users = []
        self.orders = []
        self.current_user = None

    def register_user(self, username, email, password):
        user_id = len(self.users) + 1
        user = User(user_id, username, email, password)
        self.users.append(user)
        return user

    def login_user(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                self.current_user = user
                return True
        return False

    def logout_user(self):
        self.current_user = None

    def add_product(self, name, description, price, quantity):
        product_id = len(self.products) + 1
        product = Product(product_id, name, description, price, quantity)
        self.products.append(product)
        return product

    def create_order(self, product_ids, quantities):
        if self.current_user:
            order_id = len(self.orders) + 1
            products = []
            total_amount = 0

            for product_id, quantity in zip(product_ids, quantities):
                product = self.get_product_by_id(product_id)
                if product and product.quantity >= quantity:
                    products.append({'product_id': product.product_id, 'quantity': quantity})
                    total_amount += product.price * quantity
                else:
                    return None

            order = Order(order_id, self.current_user, products, total_amount, "2024-03-01", "Pending")
            self.orders.append(order)
            return order

        return None

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def view_products(self):
        print("Product List:")
        for product in self.products:
            print(f"Product ID: {product.product_id}")
            print(f"Name: {product.name}")
            print(f"Price: ${product.price}")
            print(f"Quantity in Stock: {product.quantity}")
            print("\n")

    def view_orders(self):
        if self.current_user:
            print(f"Orders for {self.current_user.username}:")
            for order in self.orders:
                if order.user == self.current_user:
                    print(f"Order ID: {order.order_id}")
                    print(f"Date: {order.order_date}")
                    print(f"Total Amount: ${order.total_amount}")
                    print("Products:")
                    for product in order.products:
                        print(f"  - Product ID: {product['product_id']}, Quantity: {product['quantity']}")
                    print(f"Status: {order.status}")
                    print("\n")
            return True
        else:
            print("User not logged in.")
            return False

# Example usage
ecommerce_module = ECommerceModule()

# Registering a user
user1 = ecommerce_module.register_user("user1", "user1@example.com", "password")

# Logging in the user
ecommerce_module.login_user("user1@example.com", "password")

# Adding products
product1 = ecommerce_module.add_product("Laptop", "High-performance laptop", 1200.0, 50)
product2 = ecommerce_module.add_product("Printer", "Color laser printer", 300.0, 20)

# Viewing products
ecommerce_module.view_products()

# Creating an order
order1 = ecommerce_module.create_order([1, 2], [3, 1])

if order1:
    print("Order created successfully!")

# Viewing user's orders
ecommerce_module.view_orders()

# Logging out the user
ecommerce_module.logout_user()