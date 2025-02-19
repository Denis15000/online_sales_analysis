from product_manager import ProductManager
from product import Product

if __name__ == "__main__":
    # Crearea instanței ProductManager
    manager = ProductManager()
    
    # Adăugarea unor produse
    manager.add_product(Product("Laptop", 2499.99, 10))
    manager.add_product(Product("Mouse", 49.99, 50))
    manager.add_product(Product("Keyboard", 79.99, 30))
    
    # Afișarea produselor
    print("Produse disponibile:")
    print(manager.display_all_products())
    
    # Afișarea valorii totale a inventarului
    print(f"Valoarea totală a inventarului: {manager.total_inventory_value():.2f}")