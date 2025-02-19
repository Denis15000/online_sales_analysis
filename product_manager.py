from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def display_all_products(self):
        if not self.products:
            return "No products available."
        return "\n".join([product.display_info() for product in self.products])

    def total_inventory_value(self):
        return sum(product.price * product.quantity for product in self.products)

# Exemplu de utilizare
if __name__ == "__main__":
    manager = ProductManager()
    manager.add_product(Product("Laptop", 2499.99, 10))
    manager.add_product(Product("Mouse", 49.99, 50))
    print(manager.display_all_products())
    print(f"Total Inventory Value: {manager.total_inventory_value():.2f}")
