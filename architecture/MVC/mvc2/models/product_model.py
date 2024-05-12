from db import execute

class Product:
    def __init__(self, name, price, id=None):
        self.name = name
        self.price = price
        self.id = id
        self.status = 1 #active = 1, inactive = 0
        
        # if the product table does not exist, it will be created
        query = 'CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL, status NUMERIC)'
        execute(query=query)
    
    def save(self):
        query = f"INSERT INTO products (name, price, status) VALUES ('{self.name}', '{self.price}', '{self.status}')"
        execute(query=query)
    
    def update(self):
        query = f"UPDATE products SET status={int(self.status)} WHERE id={int(self.id)}"
        execute(query=query)
        
    def delete(self):
        query = f"DELETE FROM products WHERE id={int(self.id)}"
        execute(query=query)
        
    @staticmethod
    def get_products():
        query = f"SELECT * FROM products"
        products = execute(query=query)
        return products
    
    @staticmethod
    def get_product(id):
        query = f"SELECT id, name, price FROM products WHERE id={int(id)}"
        product = execute(query=query)[0]
        product = Product(id=product[0], name=product[1], price=product[2])
        return product