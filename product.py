class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        return f"Product: {self.name}, Price: {self.price:.2f}, Quantity: {self.quantity}"

    def update_quantity(self, new_quantity: int):
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            raise ValueError("Quantity cannot be negative.")

# Exemplu de utilizare
if __name__ == "__main__":
    product = Product("Laptop", 2499.99, 10)
    print(product.display_info())
    product.update_quantity(5)
    print(product.display_info())
