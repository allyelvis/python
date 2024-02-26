class RetailStoreConfiguration:
    def __init__(self, store_name, location, opening_hours, tax_rate):
        self.store_name = store_name
        self.location = location
        self.opening_hours = opening_hours
        self.tax_rate = tax_rate

    def update_store_name(self, new_name):
        self.store_name = new_name

    def update_location(self, new_location):
        self.location = new_location

    def update_opening_hours(self, new_hours):
        self.opening_hours = new_hours

    def update_tax_rate(self, new_tax_rate):
        self.tax_rate = new_tax_rate

    def display_configuration(self):
        print("Retail Store Configuration:")
        print(f"Store Name: {self.store_name}")
        print(f"Location: {self.location}")
        print(f"Opening Hours: {self.opening_hours}")
        print(f"Tax Rate: {self.tax_rate}%")

# Example usage
store_configuration = RetailStoreConfiguration(
    store_name="My Retail Store",
    location="123 Main Street",
    opening_hours="9:00 AM - 6:00 PM",
    tax_rate=8.5
)

# Display current configuration
store_configuration.display_configuration()

# Update store name
store_configuration.update_store_name("Updated Store Name")

# Update opening hours
store_configuration.update_opening_hours("10:00 AM - 7:00 PM")

# Display updated configuration
store_configuration.display_configuration()