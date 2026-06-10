class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("T-shirt", 19.99)

required_attributes = ["name", "price", "inventory_id"]

for attr in required_attributes:
    if not hasattr(product, attr):
        print(f"Error: Product is missing required attribute '{attr}'")
    else:
        print(f"{attr}: {getattr(product, attr)}")
