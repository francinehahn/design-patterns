class Model:
    def __init__(self):
        # this data would be in a db
        self.products = {
            'ps5': {'id': 1, 'name': 'PlayStation 5', 'price': 5500},
            'xbox': {'id': 2, 'name': 'Xbox 360', 'price': 5900},
            'wii': {'id': 3, 'name': 'Nintendo Wii', 'price': 4700}
        }
        
class Controller:
    def __init__(self):
        self.model = Model()
    
    def list_products(self):
        products = self.model.products.keys()
        print('------------Products------------')
        for prod in products:
            print(f'ID: {self.model.products[prod]['id']}')
            print(f'ID: {self.model.products[prod]['name']}')
            print(f'ID: {self.model.products[prod]['price']}\n')
            
class View:
    def __init__(self):
        self.controller = Controller()
        
    def products(self):
        self.controller.list_products()
        
if __name__ == '__main__':
    view = View()
    view.products()