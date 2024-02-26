class Requisition:
    def __init__(self, requisition_id, product_id, quantity_requested, status, request_date):
        self.requisition_id = requisition_id
        self.product_id = product_id
        self.quantity_requested = quantity_requested
        self.status = status  # "Pending", "Approved", "Rejected"
        self.request_date = request_date

class RequisitionModule:
    def __init__(self, inventory):
        self.requisitions = []
        self.inventory = inventory

    def create_requisition(self, product_id, quantity_requested):
        product = self.get_product_by_id(product_id)
        if product:
            requisition_id = len(self.requisitions) + 1
            requisition = Requisition(requisition_id, product_id, quantity_requested, "Pending", "2024-02-28")
            self.requisitions.append(requisition)
            return requisition
        else:
            return None

    def approve_requisition(self, requisition_id):
        requisition = self.get_requisition_by_id(requisition_id)
        if requisition and requisition.status == "Pending":
            requisition.status = "Approved"
            # Update inventory after approving requisition
            self.inventory.update_product(requisition.product_id, requisition.quantity_requested)
            return True
        else:
            return False

    def reject_requisition(self, requisition_id):
        requisition = self.get_requisition_by_id(requisition_id)
        if requisition and requisition.status == "Pending":
            requisition.status = "Rejected"
            return True
        else:
            return False

    def get_product_by_id(self, product_id):
        for product in self.inventory.products:
            if product.product_id == product_id:
                return product
        return None

    def get_requisition_by_id(self, requisition_id):
        for requisition in self.requisitions:
            if requisition.requisition_id == requisition_id:
                return requisition
        return None

    def view_requisitions(self):
        for requisition in self.requisitions:
            print(f"Requisition ID: {requisition.requisition_id}")
            print(f"Product ID: {requisition.product_id}")
            print(f"Quantity Requested: {requisition.quantity_requested}")
            print(f"Status: {requisition.status}")
            print(f"Request Date: {requisition.request_date}")
            print("\n")

# Example usage
requisition_module = RequisitionModule(inventory_system)

# Creating a requisition
created_requisition = requisition_module.create_requisition(1, 10)
if created_requisition:
    print("Requisition created successfully!")
else:
    print("Requisition creation failed. Invalid product ID.")

# Approving a requisition
approved_requisition = requisition_module.approve_requisition(1)
if approved_requisition:
    print("Requisition approved successfully!")
else:
    print("Requisition approval failed. Invalid requisition ID or already approved/rejected.")

# Rejecting a requisition
rejected_requisition = requisition_module.reject_requisition(1)
if rejected_requisition:
    print("Requisition rejected successfully!")
else:
    print("Requisition rejection failed. Invalid requisition ID or already approved/rejected.")

# Viewing requisitions
requisition_module.view_requisitions()